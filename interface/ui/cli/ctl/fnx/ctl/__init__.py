#!/usr/bin/env python

import click 	as C
from . import main
from . import ctl_disk
from . import ctl_world
from . import ctl_world_create



@C.group()
def ctl():
	"""ctl help"""
	pass

@ctl.command()
def cli():
	ctl.prompt()
 
ctl.add_command(main.ctl)
ctl.add_command(ctl_disk.disk)
ctl.add_command(ctl_world.world)