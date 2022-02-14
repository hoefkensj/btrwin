#!/usr/bin/env python
import click as C
import btrwin.fnx.check.ctl
import btrwin.fnx.conf.ctl
import btrwin.fnx.file.ctl
import fnx.fs.ctl

@C.group()
def disk():
	"""disk help"""
	pass
	
@disk.command()
def detect():
	"""
	detect disk
	:return:
	"""
	btrwin.fnx.check.ctl.detect_disk()


@disk.command()
@C.argument('id')
def select(id):
	"""
	
	:param id: id of disk to select use list to get valid id's
	:return:
	"""
	fnx.fs.ctl.fs_select_set(id=id)

@disk.command()
def list():
	"""	list valid(=mounted) btrfs volumes"""
	btrwin.fnx.file.ctl.default_disk()
	C.echo('Detected Btrfs Volumes (mounted):')
	btrwin.fnx.fs.list()