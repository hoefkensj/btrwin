#!/usr/bin/env python
from . import confctl as conf

def main():
	pass
	
	
def set(key,value,section,file):
	conf.set_setting(file=file,section=section,key=key,value=value)


if __name__ == '__main__':
	file='betterwin'
	section='PATH'
	settings={
		'mount':'/mnt/btrd0v1',
		'sys':'${mount}/opt/BTRWin',
		'subv' : '${sys}/subv',
		'loaders' : '${sys}/loaders'
	
	}
	
	
	for key in settings.keys():
		set(key,settings[key],section,file)
	
	conf.show_global_config()
	

def set_dict(dict):
	file = dict.pop('file')
	section= dict.pop('section')
	for key in dict.keys():
		set(key,dict[key],section,file)
	
		