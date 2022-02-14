#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import btrwin.lib

def create_world_config(name):
	"""
	creates the config an the configfile for the load with name
	:param name: name for the btrwinworld
	:return: the config just created
	"""
	#create the config file:
	file_world=lib.fs.touch(f'/etc/btrwin/{name}.conf')
	#initialize the config
	conf_world=fnx.conf.ctl.create_new_worldconf(name)
	#write the cofnig to the configfile
	lib.conf.savefile(file=file_world, conf=conf_world)
	#read the config again from the file
	conf_world=lib.conf.readfile(path=file_world, c=lib.conf.new())
	#set the path of the config file in  the config now that it exists:
	conf_world['PATH']['worldconfig'] = f'{file_world}'
	#save the config again and reload
	lib.conf.savefile(file=file_world, conf=conf_world)
	conf_world=lib.conf.readfile(path=file_world, c=lib.conf.new())
	return conf_world

def init_sysconf():
	file			=	'btrwin'
	section		=	'PATH'
	settings	=	{
								'file'		:		file,
								'section'	:		section,
								'config'	:		f'/etc/btrwin/{file}.conf',
								'sys'			:		'${mount}/opt/btrwin',
								'subv' 		:		'${sys}/subv',
								'loaders'	:		'${sys}/loaders'
							}