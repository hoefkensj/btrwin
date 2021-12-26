#!/usr/bin/env python
import click as C
import btrwin.dev		as dev
import btrwin.units as units

from . import btrfs as f_btrfs
from . import ctl 	as f_ctl

@C.group()
def fs():
	"""fs help"""
	pass

@fs.command()
def pkgtree():
	"""shows the filetree of this package"""
	dev.tools.pkgtree.build_tree()

@fs.command()
def list():
	"""list availeble btrfs volumes"""
	units.fs.list()
	pass

@fs.command()
@C.argument('idx')
def select(idx):
	"""select the btrfs volume to use see ..list for index numbers  """
	units.fs.select_disk(int(idx))
	pass
 
 
fs.add_command(f_btrfs.btrfs)