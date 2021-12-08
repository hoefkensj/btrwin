#!/usr/bin/env python
import click as C
import btrwin.units.fs.pkgtree
from . import btrfs as fs_btrfs

@C.group()
def fs():
	"""fs help"""
	pass

@fs.command()
def pkgtree():
	"""shows the filetree of this package"""
	btrwin.units.fs.pkgtree.build_tree()
	
 
 
 
fs.add_command(fs_btrfs.btrfs)