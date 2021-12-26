#!/usr/bin/env python
import os
import btrwin.lib 		as lib
import btrwin.units 	as unit
import btrwin.assets 	as assets

G=unit.conf.load()	#load global config in G
skels= assets.skel.skels

def sys_folders(path):
	dirs= skels.SKELLS['SYS']['DIRS']
	lib.fs.mkdirtree(dirs['sys'], path)
	
def sys_links(**k):
	links= skels.SKELLS['SYS']['LINKS']
	lib.fs.mklinktree(links, **k)

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
	
