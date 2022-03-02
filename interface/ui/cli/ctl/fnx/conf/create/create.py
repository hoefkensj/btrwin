#!/usr/bin/env python
import click as C
import os

@C.group()
def create():
	"""create help"""
	pass

@create.command()
def prefix():
	"""config for prefix"""
	import btrwin.fnx.conf.create.create
	btrwin.fnx.conf.pfx.create_prefix_config()

@create.command('rc')
def btrwinrc():
	"""a rcfile  config in ~/"""
	import btrwin.fnx.conf.create.create
	btrwin.fnx.conf.create.create.rc(f=os.path.join(os.path.expanduser('~/.config'), '.btrwinrc'))
	
@create.command('world')
@C.argument('world',default='btrwin')
@C.option('-u','--user', default=lambda: os.environ.get("USER", ""), show_default=f"{os.environ.get('USER', '')}")
def world(*a,**k):
	"""a woirld  config in /etc"""
	C.echo(repr([i for i in a  if a ]or ''))
	C.echo(repr(k))
	pass
