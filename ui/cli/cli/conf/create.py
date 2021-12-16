#!/usr/bin/env python
import click as C
from btrwin.units.conf.ctl import show_global_config



@C.group()
def create():
	"""create help"""
	pass

@create.command()
def prefix():
	"""config for prefix"""
	show_global_config()
	pass

@create.command()
def sys():
	"""the system config in /etc"""
	pass
