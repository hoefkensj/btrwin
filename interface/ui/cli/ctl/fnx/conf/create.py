#!/usr/bin/env python
import click as C
import btrwin.fnx


@C.group()
def create():
	"""create help"""
	pass

@create.command()
def prefix():
	"""config for prefix"""
	btrwin.fnx.conf.ctl.show_global_config()

@create.command()
def sys():
	"""the system config in /etc"""
	pass
