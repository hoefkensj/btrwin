#!/usr/bin/env python
import click as C
import dev.tools.pkgtree
from . import btrfs as fs_btrfs
from btrwin.units import fs as FS

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
	FS.list()
	pass


@fs.command()
@C.argument('idx')
def select(idx):
	"""select the btrfs volume to use see ..list for index numbers  """
	FS.select_disk(int(idx))
	pass
 
 
fs.add_command(fs_btrfs.btrfs)