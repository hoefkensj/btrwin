#!/usr/bin/env python
import click as C
from . import create as  setup_create

import btrwin.units.fs

@C.group()
def setup():
	"""setup help"""
	pass

@setup.command()
def pkgtree():
	"""shows the filetree of this package"""
	btrwin.units.fs.pkgtree.build_tree()
	
 
 
 
