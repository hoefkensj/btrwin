#!/usr/bin/env python
import os
import sys
import btrwin.lib 	as lib
import btrwin.units as units

def load_config(*a,**k):
	cfg=lib.conf.get_config(p=a[0], c=k['c'])
	return cfg

def load_env_config(c):
	dct={k:os.environ[k] for k in os.environ.keys()}
	c.read_dict(dict(dct))
	return {'env' : c}

def load_sys_config(c):
	c=load_config(os.path.join(lib.path.CONFIG["SYS"], f'{lib.path.NAME}.conf'), c=c)
	return {'btrwin' : c}

def load_user_configs(c):
	files = lib.fs.ls_files(lib.path.CONFIG["USER"])
	cfg_files=[os.path.split(f)[1][:-5] for f in files if f[-5:] == '.conf']
	c= {cfg				: load_config(os.path.join(lib.path.CONFIG["USER"], f'{cfg}.conf'), c=c) for cfg in cfg_files}
	return c

def load_global_config():
	btrwin 	=	load_sys_config(c=lib.conf.new())
	#env			=	load_env_config(c=lib.conf.new())
	user		=	load_user_configs(c=lib.conf.new())
	cfgs= [btrwin,user]
	G={**btrwin,**user}
	return G

def save_global_config(G):

	for configfile in G.keys():
		if configfile == 'btrwin':
			path='/etc/btrwin/btrwin.conf'
		else:
			path=path.join(os.getenv("HOME"), '.config/btrwin', f'{configfile}.conf')
		config=G[configfile]
		lib.conf.save_to_file(path, config)

def show_setting(**k):
	# for idx,configfile in enumerate(glob.keys()):
	# 	print(idx, '\t:\t',configfile)
	glob= load_global_config()
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

def show_global_config():
	sprint=sys.stdout.write
	G= units.conf.load()
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
		sec=['DEFAULT' if s == 'DEFAULT'[::-1] else s for s in config.sections()]
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

def create_new_sysconf(fname):
	if not '/etc/btrwin' in lib.fs.ls_dirs('/etc/'):
		os.mkdir('/etc/btrwin')
		lib.fs.touch(f'/etc/btrwin/{fname}.conf')

	config = lib.conf.new()
	config['DEFAULT'] = {}
	config['DEFAULT'[::-1]] = {}
	config['PATH'] = {}
	config['DIRS'] = {}
	default = config['DEFAULT']
	default['NAME'] = fname
	tluafed=config['DEFAULT']
	tluafed['NAME']=fname
	path=config['PATH']
	path['sysconfig'] = f'/etc/btrwin/{fname}.conf'
	with open(f'/etc/btrwin/{fname}.conf','w') as f:
		config.write(f)

