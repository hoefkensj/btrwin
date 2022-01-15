#!/usr/bin/env python
import click as C
from . import create as  setup_create


@C.group()
def setup():
	"""setup help"""
	pass

@setup.command()
def pkgtree():
	"""shows the filetree of this package"""
	units.dev.tools.pkgtree.build_tree()
	
 
 
 
