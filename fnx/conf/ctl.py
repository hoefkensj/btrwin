#!/usr/bin/env python
import os
import sys
import functools

import btrwin.lib
import btrwin.fnx.conf.load.ctl


def show_setting(**k):
	# for idx,configfile in enumerate(glob.keys()):
	# 	print(idx, '\t:\t',configfile)
	glob= btrwin.fnx.conf.load.ctl.global_config()
	if  k.get('file'):
		file = k['file']
		print(f'|->{file}/')
		config=glob[file]
		
		if k.get('section'):
			section=k['section']
			print(f'|\t|->{section}:')
			#print(config.sections())
			if section in config.sections():
				#print(glob[file][section])
				if 'key' in k:
					key=k['key']
					if key in config[section].keys():
						print(f'|\t|\t|->{key}\t:\t{glob[file][section][key]}')
						print()
					else:
						print('key does not exist')
				else:
					print(dict(glob[file][section]).keys())
			else:
				print('section does not exist')
		#print({section: dict(config[section]) for section in config.sections()})
		else:
			for section in config.sections():
				print(f'|\t|->[{section}]')
	else:
		print(glob.keys())

def show_world_config(**k):
	world=k.get('W')
	k['c']=btrwin.lib.conf.new() #use new configparser config as to not to replace the active one in glob config!
	sprint=sys.stdout.write
	c= btrwin.fnx.conf.load.ctl.world_config(**k)
	
	def unpack(cfg):
		for item in cfg:
			print(item)

	
	unpack(c)
	
	
	def s_fx():
		"""
		is string_fix is string_prefix + string_suffix for config:show
		:return: list(f,s,o) where list(x) is tuple(prefix,suffix) for f=file,s=section,o=option
		"""
		fx	=	(	('|---<<','>>'),
						('|----[',']'		),
						('|---> ',''		),)
		return fx[0],fx[1],fx[2]
		
	
	char=0
	sf,ss,so=s_fx()
	for file in G.keys():
		print(f"{sf[0]}{file}{sf[1]}")
		config=G[file]
		### [DEFAULT]-section HACK ###
		# see DOC[HACKS]:configparser
			#	if the config has a [default] section it should also have a dummy [tluafed] section if so , add it to the sections list
			#	this is a needed hack  as config.sections() does not include the [default] section
		sec=[]
		try:
			if config['DEFAULT']:
				sec= ['DEFAULT',]
		except KeyError:
			pass
		except TypeError:
			pass
		sec+=[ s for s in config.sections()]
		#since [default] is first in the config lets make it appear first aswell when config:show
		sections=[sec.pop(sec.index('DEFAULT'))]+sec if 'DEFAULT' in sec else sec
		for section in sections:
			print(f'|\t{ss[0]}{section}{ss[1]}')
			sect=config[section]
			for key in dict(sect).keys():
				char= len(key) if len(key) > char else char
				line=''
				line='|\t|\t'
				line+=f'{so[0]}{key}'
				line+=' '*(char-len(key))
				line+=' '*1
				line+=':\t'
				line+=f'{sect[key]}{so[1]}\n'
				sprint(line)
			print(f'|\t|')
		print(f'|')

def show_global_config():
	sprint=sys.stdout.write
	G= btrwin.fnx.conf.ctl.load()
	def s_fx():
		"""
		is string_fix is string_prefix + string_suffix for config:show
		:return: list(f,s,o) where list(x) is tuple(prefix,suffix) for f=file,s=section,o=option
		"""
		fx	=	(	('|---<<','>>'),
						('|----[',']'		),
						('|---> ',''		),)
		return fx[0],fx[1],fx[2]
		
	char=0
	sf,ss,so=s_fx()
	for file in G.keys():
		print(f"{sf[0]}{file}{sf[1]}")
		config=G[file]
		### [DEFAULT]-section HACK ###
		# see DOC[HACKS]:configparser
			#	if the config has a [default] section it should also have a dummy [tluafed] section if so , add it to the sections list
			#	this is a needed hack  as config.sections() does not include the [default] section
		sec=[]
		try:
			if config['DEFAULT']:
				sec= ['DEFAULT',]
		except KeyError:
			pass
		except TypeError:
			pass
		sec+=[ s for s in config.sections()]
		#since [default] is first in the config lets make it appear first aswell when config:show
		sections=[sec.pop(sec.index('DEFAULT'))]+sec if 'DEFAULT' in sec else sec
		for section in sections:
			print(f'|\t{ss[0]}{section}{ss[1]}')
			sect=config[section]
			for key in dict(sect).keys():
				char= len(key) if len(key) > char else char
				line=''
				line='|\t|\t'
				line+=f'{so[0]}{key}'
				line+=' '*(char-len(key))
				line+=' '*1
				line+=':\t'
				line+=f'{sect[key]}{so[1]}\n'
				sprint(line)
			print(f'|\t|')
		print(f'|')

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

