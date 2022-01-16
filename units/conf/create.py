#!/usr/bin/env python
import os
import types
import btrwin.lib as lib

def sys_sdir() -> None:
	if 'btrwin' in lib.fs.ls_A('/etc/'):
		if os.path.isfile('/etc/btrwin') or os.path.isdir('/etc/btrwin') :
			os.rename('/etc/btrwin','/etc/btrwin.backup')
			sys_sdir()
	else:
		os.mkdir('/etc/btrwin')
		lib.fs.touch(f'/etc/btrwin/installed_env.conf')

def sys_file(fname) -> None:
	lib.fs.touch(f'/etc/btrwin/{fname}.conf')
	with open(f'/etc/btrwin/{fname}.conf') as c:
		c.write(f'#\tFILE:\t/etc/btrwin/{fname}.conf#')
	
def sys_conf(fname):
	config 													= 	lib.conf.new()
	config['DEFAULT'] 							= 	{}
	config['DEFAULT']['name'] 			= 	fname
	config['PATH'] 									= 	{}
	config['PATH']['sysconfig'] 		= 	f'/etc/btrwin/{fname}.conf'
	config['CONFIG']								= 	{}
	config['CONFIG']['name'] 				= 	fname
	config['CONFIG']['file'] 				= 	f'{fname}.conf'
	config['CONFIG']['created']			= 	lib.func.NOW.stamp
	config['DIRS'] 									= 	{}
	return config
	
def sys_cffl(config):      #= sys_conf-file
	with open(f'/etc/btrwin/{fname}.conf','w') as f:
		config.write(f)

def sys_allc(fname) -> None:
	sys_sdir()
	sys_file(fname)
	sys_config=sys_conf(fname)
	sys_cffl(sys_config)
	
def sys():
	sys=types.SimpleNamespace
	sys.sdir				=		sys_sdir
	sys.file				=		sys_file
	sys.conf				=		sys_conf
	sys.cffl				=		sys_cffl
	sys.allc 				=		sys_allc
	return sys