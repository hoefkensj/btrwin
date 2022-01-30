#!/usr/bin/env python
import os

import btrwin.lib as lib
def sys_sdir() -> None:
	if 'btrwin' in lib.fs.ls_A('/etc/'):
		if os.path.isfile('/etc/btrwin') or os.path.isdir('/etc/btrwin') :
			os.rename('/etc/btrwin','/etc/btrwin.backup')
			sys_sdir()
	else:
		os.mkdir('/etc/btrwin')
		lib.fs.touch(f'/etc/btrwin/installed_env.conf')

def sys_file(name) -> None:
	lib.fs.touch(f'/etc/btrwin/{name}.conf')
	with open(f'/etc/btrwin/{name}.conf') as c:
		c.write(f'#\tFILE:\t/etc/btrwin/{name}.conf#')
	
def sys_conf(name):
	config 													= 	lib.conf.new()
	config['DEFAULT'] 							= 	{}
	config['DEFAULT']['name'] 			= 	name
	config['PATH'] 									= 	{}
	config['PATH']['sysconfig'] 		= 	f'/etc/btrwin/{name}.conf'
	config['CONFIG']								= 	{}
	config['CONFIG']['name'] 				= 	name
	config['CONFIG']['file'] 				= 	f'{name}.conf'
	config['CONFIG']['created']			= 	lib.func.NOW.stamp
	config['DIRS'] 									= 	{}
	return config
	
def sys_cffl(config):      #= sys_conf-file
	name=config['DEFAULT']['NAME']
	with open(f'/etc/btrwin/{name}.conf','w') as f:
		config.write(f)

def sys_allc(name) -> None:
	sys_sdir()
	sys_file(name)
	sys_config=sys_conf(name)
	sys_cffl(sys_config)
	
