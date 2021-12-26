#!/usr/bin/env python
import click as C
import btrwin.dev as dev
from . import create as  setup_create


@C.group()
def setup():
	"""setup help"""
	pass

@setup.command()
def pkgtree():
	"""shows the filetree of this package"""
	dev.tools.pkgtree.build_tree()
	
 
 
 
