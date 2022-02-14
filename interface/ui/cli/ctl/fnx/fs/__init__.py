#!/usr/bin/env python
import click as C


from . import btrfs
from . import ctl

@C.group()
def fs():
	"""fs help"""
	pass




@fs.command()
def list():
	"""list volumes"""
	import btrwin.fnx.fs.ctl
	btrwin.fnx.fs.ctl.list()




 
fs.add_command(btrfs.btrfs)
fs.add_command(ctl.select)