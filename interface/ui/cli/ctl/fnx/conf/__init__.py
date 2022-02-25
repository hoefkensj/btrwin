#!/usr/bin/env python
import click 	as C

from . import show
from . import create
from . import ctl
from . import main
from . import load

@C.group()
def conf():
	"""conf help"""
	pass

@conf.command()
def paths():
	import btrwin.fnx.conf.ctl
	btrwin.fnx.conf.ctl.show_config_paths()
 
conf.add_command(show.show)
conf.add_command(create.create)
conf.add_command(ctl.ctl)
conf.add_command(load.load.load())