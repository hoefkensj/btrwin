#!/usr/bin/env python
import click as C
from . import ctl_world
from . import ctl_disk

@C.group()
def ctl():
	"""ctl help"""

	pass
	
ctl.add_command(ctl_disk.disk)
ctl.add_command(ctl_world.world)



