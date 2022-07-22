#!/usr/bin/env python
import click as C
import btrwin.modules.conf.ctl

from . import ctl_world_create
@C.group()
def world():
	"""load help"""
	pass
	
@world.command()
@C.argument('load')
def activate(world):
	"""
	activate load with name
	:param world: name of load
	:return:
	"""
	WORLD= btrwin.modules.conf.ctl.activate_world(world)
	C.echo(WORLD)


world.add_command(ctl_world_create.create)

