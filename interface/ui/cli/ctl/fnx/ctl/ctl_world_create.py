#!/usr/bin/env python
import click as C
import btrwin.modules.conf.create.ctl
import btrwin.fnx.file.create.ctl
@C.group()
def create():
	"""
	
	:return:
	"""
	pass

@create.command()
@C.argument('name')
def config(name):
	"""
	creates the config an the configfile for the load with name
	:param name: name for the btrwinworld
	:return: the config just created
	"""
	btrwin.fnx.conf.create.create.ctl.create_world_config(name)
	
@create.command()
@C.argument('name')
@C.argument('path')
def system(name,path):
	"""
	create the folder/link structure/tree  for the load with name Name
	:param path: base path upon where to create the load system
	:param name: namme of the load
	:return:
	"""
	btrwin.fnx.file.create.ctl.create_world_system(name=name, path=path)
	
