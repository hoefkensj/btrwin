#!/usr/bin/env python
import click as C
import btrwin.fnx
import os

@C.group()
def create():
	"""create help"""
	pass

@create.command()
def prefix():
	"""config for prefix"""
	btrwin.fnx.conf.ctl.show_global_config()

@create.command('btrwinrc')
def btrwinrc():
	"""a rcfile  config in ./"""
	import btrwin.fnx.conf.create.create
	btrwin.fnx.conf.create.create.btrwinrc()
	
@create.command('world')
@C.argument('world')
@C.option('-u','--user', prompt=True, default=lambda: os.environ.get("USER", ""), show_default=f"{os.environ.get('USER', '')}")
def world(*a,**k):
	"""a woirld  config in /etc"""
	C.echo(repr([i for i in a  if a ]or ''))
	C.echo(repr(k))
	pass
