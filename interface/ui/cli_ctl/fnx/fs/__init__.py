#!/usr/bin/env python
import click as C
import btrwin.fnx


from . import btrfs
from . import ctl

@C.group()
def fs():
	"""fs help"""
	pass

@fs.command()
def list():
	"""list availeble btrfs volumes"""
	fnx.fs.list()


@fs.command()
@C.argument('idx')
def select(idx):
	"""select the btrfs volume to use see ..list for index numbers  """
	fnx.conf.ctl.select_disk(int(idx))

 
 
fs.add_command(btrfs.btrfs)
fs.add_command(ctl.ctl)