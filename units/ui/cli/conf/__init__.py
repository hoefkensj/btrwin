#!/usr/bin/env python
import click 	as C

from . import show 		as c_show
from . import create 	as c_create
from . import ctl			as c_ctl


@C.group()
def conf():
	"""conf help"""
	pass
 
conf.add_command(c_show.show)
conf.add_command(c_create.create)
conf.add_command(c_ctl.ctl)