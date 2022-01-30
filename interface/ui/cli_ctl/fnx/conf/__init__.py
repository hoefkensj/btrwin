#!/usr/bin/env python
import click 	as C
import btrwin.fnx

from . import show 		as c_show
from . import create 	as c_create
from . import ctl			as c_ctl
from . import conf		as c_conf


@C.group()
def conf():
	"""conf help"""
	pass

@conf.command()
def show():
	fnx.conf.show()
 
conf.add_command(c_show.show)
conf.add_command(c_create.create)
conf.add_command(c_ctl.ctl)