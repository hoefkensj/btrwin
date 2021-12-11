#!/usr/bin/env python
from btrwin import G
from btrwin.assets import skel
from btrwin.units import fs
import btrwin.debug as d

G=G()	#load global config in G

def sys_folders(path):
	DIRS= skel.sys.dirs()
	F.create_dtree(DIRS['sys'],path)
	d.print('dirs created')
	skel.tpl.lnks(path)
	d.print('symlinks created')


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
	
def seq():
	fs.list()
	sprint