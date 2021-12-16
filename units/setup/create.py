#!/usr/bin/env python
import btrwin.lib as lib
import btrwin.assets.skel as skel
import btrwin.units.conf as c
import os

G=c.get()	#load global config in G

def sys_folders(path):
	DIRS=skel.sys.DIRS
	lib.fs.mkdirtree(DIRS['sys'], path)
	

def sys_links(path):
	LINKS=skel.sys.links(path)
	lib.fs.mklinktree(LINKS, path)


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
	
