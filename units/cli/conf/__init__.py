#!/usr/bin/env python
import click as C
from . import show as conf_show
from . import create as conf_create

@C.group()
def conf():
	"""fs help"""
	pass


	
 
 
 
conf.add_command(conf_show.show)
conf.add_command(conf_create.create)