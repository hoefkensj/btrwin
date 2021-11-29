#!/usr/bin/python3

import click as C
#from betterwin.pfx import scan


@C.command()
@C.argument('name',required=1)
def new(name):
	'''create a new prefix '''
	pass

@C.command()
@C.argument('name',required=1)
def scan(name):
	'''name of the prefix '''
	from . import scan as scanpfx

	def name(name):
		'''name of pfx'''
		scanpfx(name)
		C.echo(name)

@C.command()
def list():
	'''List prefixes '''
	from . import list as listall
	listall.list()
	
	
@C.group()
def pfx():
	pass




pfx.add_command(new)
pfx.add_command(scan)
pfx.add_command(list)


if __name__ == '__main__':
	pfx(prog_name='pfx')
	










# @action.command()
# @action.argument('tpl', help='template to use as src',default='tpl-Win64_20211121v1' )
# @action.argument('name', help='new prefix name')
# def create(name,tpl):
# 	pfx.new.create_new_prefix(cli.config.create.name,cli.config.create.tpl)
#
#
# @action.command()
# @action.argument('ext',choices=['exe','lnk'], help='scan for exe or lnk' )
# @action.argument('prefix', help='prefix to scan name')
# def scann(prefix, ext):
# 	pfx.scan.scn_ext(prefix,ext,data=[])
#
# @action.command()
# @action.argument('tpl', help='template to use as src',default='tpl-Win64_20211121v1' )
# @action.argument('name', help='new prefix name')
# def create(cli):
# 	pfx.new.create_new_prefix(cli.config.create.name,cli.config.create.tpl)
#
# @action.command()
# @action.argument('tpl', help='template to use as src',default='tpl-Win64_20211121v1' )
# @action.argument('name', help='new prefix name')
# def create(cli):
# 	pfx.new.create_new_prefix(cli.config.create.name,cli.config.create.tpl)
#
#
#
#
#
#

#
# if __name__ == '__main__':
#     cli()