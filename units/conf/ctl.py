#!/usr/bin/env python
from configparser import ConfigParser,ExtendedInterpolation
import os
import argparse


def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option
	return cfg
	
def get_dirs(parent):
	dirs=[os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
	return dirs

def get_config(**k):
	config=k['config']
	path=k['path']
	config.read(path)
	return config
	
def save_to_file(file,conf):
	with open(file, 'w') as file:
		conf.write(file)
	return
	
def construct_global_config():
	glob={}
	files=[]
	path='/etc/betterwin/betterwin.conf'
	glob['btrwin'] = get_config(path=os.path.join(path),config=new())
	path=os.path.join(os.getenv("HOME"),'.config/btrwin.conf') #=the folder ...btrwin.conf/configs..
	files += [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	cfg_files=[f for f in files if f[-5:] == '.conf']
	for cfg in cfg_files:
		glob[cfg[:-5]] = get_config(path=os.path.join(path,cfg),config=new())
	return glob

def save_global_config(glob):
	for configfile in glob.keys():
		if configfile == 'btrwin':
			path='/etc/betterwin/betterwin.conf'
		else:
			path=os.path.join(os.getenv("HOME"),'.config/btrwin.conf',f'{configfile}.conf')
		config=glob[configfile]
		save_to_file(path,config)
		
def get_global_config():
	return construct_global_config()

def show_setting(**k):
	# for idx,configfile in enumerate(glob.keys()):
	# 	print(idx, '\t:\t',configfile)
	glob= get_global_config()
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
	glob=get_global_config()
	tabs=0
	for file in glob.keys():
		print(f'|---<{file}>')
		file=glob[file]
		for section in file.sections():
			print(f'|\t|---[{section}]')
			for key in dict(file[section]).keys():
				tabs= divmod(len(key),4)[0] if divmod(len(key),4)[0] > tabs else tabs
				if divmod(len(key),2)[0] == tabs:
					print(f'|\t|\t|---> {key}',' ',f':\t{file[section][key]}')
				elif divmod(len(key),2)[0] == tabs-1:
					print(f'|\t|\t|---> {key}','\t',f':\t{file[section][key]}')
				elif divmod(len(key),2)[0] == (tabs-2):
					print(f'|\t|\t|---> {key}','\t',f':\t{file[section][key]}')
			print(f'|\t|')
		print(f'|')

def set_setting(**k):
	glob=get_global_config()
	file = k.get('file')
	section=k.get('section')
	key=k.get('key')
	val=k.get('value')
	
	if file:
		config=glob[file] if glob.get(file) else new()
		config[section]= glob[file][section] if dict(config).get(section) else {}
		config[section][key]=val
		glob[file]=config
		save_global_config(glob)
		return glob


	else :
		return 1 # error = 1

def qset(key,value,section,file):
	set_setting(file=file,section=section,key=key,value=value)

def set_dict(dict):
	file = dict.pop('file')
	section= dict.pop('section')
	for key in dict.keys():
		qset(key,dict[key],section,file)



