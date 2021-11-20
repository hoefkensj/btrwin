#!/usr/bin/env python
from configparser import ConfigParser,ExtendedInterpolation
import os


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
	glob['betterwin'] = get_config(path=os.path.join(path),config=new())
	path=os.path.join(os.getenv("HOME"),'.config/betterwin.conf')
	files += [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	cfg_files=[f for f in files if f[-5:] == '.conf']
	for cfg in cfg_files:
		glob[cfg[:-5]] = get_config(path=os.path.join(path,cfg),config=new())
	return glob

def save_global_config(glob):
	for configfile in glob.keys():
		if configfile == 'betterwin':
			sudopath='/etc/betterwin/betterwin.conf'
			continue
		else:
			path=os.path.join(os.getenv("HOME"),'.config/betterwin.conf',f'{configfile}.conf')
		config=glob[configfile]
		save_to_file(path,config)
		
def show_setting(glob,**k):
	# for idx,configfile in enumerate(glob.keys()):
	# 	print(idx, '\t:\t',configfile)
	if 'file' in k:
		file = k['file']
		print(f'|->{file}/')
		config=glob[file]
		if 'section' in k:
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
		print(glob.keys())

def set_setting(glob,**k):
	if 'file' in k:
		file = k['file']
		print(f'|->{file}/')
		if file not in glob.keys():
			glob[file]=new()
		config=glob[file]
		section=k['section']
		print(f'|\t|->{section}:')
		if section not in config.sections():
			glob[file][section]={}
		key=k['key']
		val=k['value']
		glob[file][section][key]=val
		print(f'|\t|\t|->{key}\t:\t{glob[file][section][key]}')
		save_global_config(glob)
		return glob

set_setting(construct_global_config(),file='file2' , section='test', key='keya',value='testb')
show_setting(construct_global_config(),file='file2' , section='test', key='keya')

