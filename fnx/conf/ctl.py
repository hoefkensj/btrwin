#!/usr/bin/env python
import os

import btrwin.lib
import btrwin.fnx.conf.load.ctl

def create_sys_config_dir():
	if not '/etc/btrwin' in btrwin.lib.fs.ls_dirs('/etc/'):
		os.mkdir('/etc/btrwin')

def create_new_worldconf(name):
	config = btrwin.lib.conf.new()
	config['DEFAULT'] = {}
#	config['DEFAULT'[::-1]] = {} #default sextion listing hack
	config['PATH'] = {}
	config['DIRS'] = {}
	config['DEFAULT']['WORLD']=name.upper()
	config['CONFIG']['name'] = name
	config['CONFIG']['file'] = f'{name}.conf'
	config['CONFIG']['created']= btrwin.lib.func.NOW.stamp
	return config
	
	# config['PATH']['worldconfig'] = f'/etc/btrwin/{fname}.conf'
	#
	#
	#
	# with open(f'/etc/btrwin/{fname}.conf','w') as f:
	# 	config.write(f)

def load_sys_config():	return btrwin.fnx.conf.load.ctl.sys_config(c=btrwin.lib.conf.new())
def load_user_configs():return btrwin.fnx.conf.load.ctl.user_configs(c=btrwin.lib.conf.new())
def load_env_config():	return btrwin.fnx.conf.load.ctl.env_config(c=btrwin.lib.conf.new())

def activate_world(name):
	"""
	set a load config as the active one
	:param name: name of the load config to activate
	:return: the Active World name
	"""
	os.environ["BTRWIN_WORLD_ACTIVE"]=name
	WORLD=os.environ.get('BTRWIN_WORLD_ACTIVE')
	G=btrwin.fnx.conf.load()
	return WORLD

