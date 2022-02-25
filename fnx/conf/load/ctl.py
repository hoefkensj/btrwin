#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import os
import btrwin.lib

def config(**k):
	"""
	loads configparser config
	:param k: path,conf
	:keyword path: path of config
	:keyword c: configparser
	:return: config
	"""
	k['c']=btrwin.lib.conf.new() if not k.get('c') else k.get('c')
	return btrwin.lib.conf.readfile(**k)

def running_config():
	btrwinrc=os.path.join(os.path.dirname(__file__),'.btrwinrc')
	c=config(f=btrwinrc,c=btrwin.lib.conf.new())
def env_config(c):
	env_config={}
	env_config['BTRWIN']={}
	for key in os.environ.keys():
		if key.startswith('BTRWIN'):
			env_config['BTRWIN'][key]=os.environ.get(key)
		elif key.startswith('WINE'.casefold()):
			env_config['WINE'][key]=os.environ.get(key)
		elif key.startswith('PROTON'.casefold()):
			env_config['PROTON'][key]=os.environ.get(key)
		elif key.startswith('CXOFFICE'.casefold()):
			env_config['CXOFFICE'][key]=os.environ.get(key)

	c.read_dict(dict(dct))
	return {'env' : c}

def world_config(**k):
	world=k.get('W')
	c=k.get('c')
	c=config(path=os.path.join(assets.path.CONFIG["SYS"], f'{world}.conf'), c=c)
	return c

def sys_config(**k):
	WORLD=os.environ.get("BTRWIN_WORLD_ACTIVE")
	config=btrwin.lib.conf.new()
	sys_cfg=world_config(world=WORLD, c=config)
	return {f'{WORLD}' : sys_cfg}

def user_configs():
	files = btrwin.lib.fs.ls_files(assets.path.CONFIG["USER"])
	cfg_files=[os.path.split(f)[1][:-5] for f in files if f[-5:] == '.conf']
	user_cfg = {cfg				: config(os.path.join(assets.path.CONFIG["USER"], f'{cfg}.conf')) for cfg in cfg_files}
	return user_cfg

def global_config():
	"""
	global config = dict
			structure:
			GLOBALCONFIG = { SYSTEM	: {
																	ACTIVEWORLD: WORLD_CONFIG,
																},
											USER		: {
																	CONfIGNAME:	NAME_CONFIG,
																},
											},
	:return: dict Global_Config
	"""
	system	= {'SYSTEM' :	sys_config(),},
	#env			=	load_env_config(c=btrwin.lib.conf.new())
	user		=	{'USER'		:	user_configs(),},

	G={}
	G['SYSTEM']	= system
	G['USER']		= user
	#G={**btrwin,**user}
	return G