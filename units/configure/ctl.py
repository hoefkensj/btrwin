#!/usr/bin/env python
import os
import time
import types

import click as C
import colorama as col
import btrwin.assets as assets
import btrwin.lib as lib
import btrwin.units as units

def create_name(name):
	sys_conf = units.conf.load_sys
	if os.path.isfile(f'/etc/btrwin/{name}.conf'):
		with open(f'/etc/btrwin/{name}.conf') as test:
			try:
				sys_conf = sys_conf()
				sys_conf.get(['btrwin']['PATH']['mount'])
				exists = True
			except KeyError:
				exists = False
	if not exists:
		lib.fs.touch(f'/etc/btrwin/{name}.conf')
		units.conf.ctl.create_new_sysconf(name)
	return name

def select_disk(id):
	valid,idxsld = detect_disk()

	disk = 0
	while disk not in range(1, valid + 1):
		disk = id
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			units.fs.list()
	units.fs.select_disk(disk)
	return units.fs.get_list()[disk - 1][1]

def detect_disk():
		valid = 0
		for idx, dsk in enumerate(lib.fs.ls_disks('btrfs')):
			valid = idx + 1
		return valid
		
def default_disk():
	return [idx + 1 for idx, dsk in enumerate(lib.fs.ls_disks('btrfs'))	if units.fs.selected_disk() in dsk[1]]
	