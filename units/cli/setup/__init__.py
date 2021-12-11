#!/usr/bin/env python
import click as C
from . import create as  setup_create

from btrwin.units.fs import pkgtree

@C.group()
def setup():
	"""setup help"""
	pass

@setup.command()
def pkgtree():
	"""shows the filetree of this package"""
	pkgtree.build_tree()
	
 
 
 
