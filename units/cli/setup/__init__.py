#!/usr/bin/env python
import click as C
from . import create as  setup_create

@C.group()
def setup():
	"""fs help"""
	pass

@setup.command()
def pkgtree():
	"""shows the filetree of this package"""
	btrwin.units.fs.pkgtree.build_tree()
	
 
 
 
fs.add_command(setup_create.btrfs)