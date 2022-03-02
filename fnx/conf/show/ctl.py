#!/usr/bin/env python
import sys

import fnx
import lib

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
	for file in c.keys():
		print(f"{sf[0]}{file}{sf[1]}")
		config=c[file]
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
		sec+=[ s for s in config.keys()]
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
	import btrwin.fnx.conf.load.ctl
	sprint=sys.stdout.write
	
	G= btrwin.fnx.conf.load.ctl.global_config()
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
		sec+=[ s for s in dict(config)]
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

def show_rc_config(**k):
	import btrwin.lib.conf
	k['c']=btrwin.lib.conf.new() #use new configparser config as to not to replace the active one in glob config!
	sprint=sys.stdout.write
	c= btrwin.fnx.conf.load.ctl.running_config()
		

		
		
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
	for file in c.keys():
		print(f"{sf[0]}{file}{sf[1]}")
		config=c[file]
		### [DEFAULT]-section HACK ###
		# see DOC[HACKS]:configparser
			#	if the config has a [default] section it should also have a dummy [tluafed] section if so , add it to the sections list
			#	this is a needed hack  as config.sections() does not include the [default] section
		sec=[]
		try:
			if 'DEFAULT' in config:
				sec += ['DEFAULT']
		except KeyError:
			pass
		except TypeError:
			pass
		sec+=[ s for s in config]
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