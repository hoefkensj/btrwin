#!/usr/bin/env python
from configparser import ConfigParser, ExtendedInterpolation

def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

def set(key,value,section,file):
	set_key(file=file, section=section, key=key, value=value)
	
def get_config(**k):
	config=k['c']
	path=k['p']
	config.read(path)
	return config

def save_to_file(file,conf):
	with open(file, 'w') as file:
		conf.write(file)
	return

def set_key(**k):
	glob=k.get('config')
	file = k.get('file')
	section=k.get('section')
	key=k.get('key')
	val=k.get('val')
	if file:
		config=glob[file] if glob.get(file) else new()
		config[section]= glob[file][section] if dict(config).get(section) else {}
		config[section][key]=str(val)
		glob[file]=config
		return glob


	else :
		return 1 # error = 1

def set_dict(dct,cfg):
	"""
	loads a dictionary formatted config group into the config ,
	the dictionary needs to meet the following specifications:
	the first two key:val pairs are file:<filename >and section:<section-name> within the file
	example:
	config={file : btrwin,
					section: PATH,
					key1: val1}
	:param dct: dictionary where the first two key:val pairs are file:filename and section within the file
	:return:
	"""
	file = dct.pop('file')
	section= dct.pop('section')
	[set_key(key=key,val=dct[key],section=section,file=file,config=cfg) for key in dct.keys()]