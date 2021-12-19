#!/usr/bin/env python
import btrwin.lib as lib
import btrwin.assets.skel as skel
import btrwin.units as unit
import os

G=unit.conf.get()	#load global config in G

def sys_folders(path):
	DIRS=skel.skels.SKELLS['SYS']['DIRS']
	lib.fs.mkdirtree(DIRS['sys'], path)
	

def sys_links(**k):
	LINKS=skel.skels.SKELLS['SYS']['LINKS']
	lib.fs.mklinktree(LINKS, **k)

def init_sysconf():
	file='btrwin'
	section='PATH'
	settings={
		'file': file,
		'section': section,
		'config': f'/etc/btrwin/{file}.conf',
		'sys':'${mount}/opt/btrwin',
		'subv' : '${sys}/subv',
		'loaders' : '${sys}/loaders'
	}
	
