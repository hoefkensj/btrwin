#!/usr/bin/env python
from btrwin.units.conf import ctl


def set(key,value,section,file):
	ctl.set_setting(file=file,section=section,key=key,value=value)

def set_dict(dict):
	file = dict.pop('file')
	section= dict.pop('section')
	for key in dict.keys():
		set(key,dict[key],section,file)

def init():
	file='btrwin'
	section='PATH'
	settings={
		'mount':'/mnt/btrd0v1',
		'sys':'${mount}/opt/BTRWin',
		'subv' : '${sys}/subv',
		'loaders' : '${sys}/loaders'
	}
	for key in settings.keys():
		set(key,settings[key],section,file)
	return

if __name__ == '__main__':
	init()
	