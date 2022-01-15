#!/usr/bin/env python
import os
import time
import types

import click as C
import colorama as col
import btrwin.assets as assets
import btrwin.lib as lib
import btrwin.units as units
import btrwin.tools.portal.portal
portal= btrwin.tools.portal.portal.portal

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
	valid = detect_disk()
	if id  in range(1, valid + 1):
		units.fs.select_disk(id)
		done=True
	else:
		done=False
	return done

def detect_disk():
		valid = 0
		for idx, dsk in enumerate(lib.fs.ls_disks('btrfs')):
			valid = idx + 1
		return valid
		
def default_disk():
	return [idx + 1 for idx, dsk in enumerate(lib.fs.ls_disks('btrfs'))	if units.fs.selected_disk() in dsk[1]]
	
def setup_sys(mount, pth):
	USERHOME = os.environ.get('HOME')
	USER = os.environ.get('USER')
	PATH = os.path.join(mount, pth)
	units.setup.create.sys_folders(PATH)
	units.setup.create.sys_links(USERHOME=USERHOME, USER=USER, PATH=PATH)
	
def collect_runners():
	FPATH = f'{k["PATH"]}/{k["NAME"]}/loaders/wine'
	src_master = f'{os.environ.get("HOME")}/.local/share/lutris/runners/wine'
	runners = lib.fs.ls_dirs(src_master)
	for runner in runners:
		portal(runner, coldir,'link',force=True,rel=False)