#!/usr/bin/env python
import click as C


@C.group()
def select():
	"""select a filesystem to use"""
	pass

@select.command()
def list():
	"""list valid/ready/usable filesystems , selected filesystem is marked with a '*'"""
	import btrwin.fnx.fs.ctl
	btrwin.fnx.fs.ctl.list()

@select.command()
@C.argument('idx')
def set(idx):
	"""select the btrfs volume to use ,see list for index numbers  """
	import btrwin.fnx.fs.ctl
	btrwin.fnx.fs.ctl.fs_select_set(idx=int(idx))