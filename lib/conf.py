#!/usr/bin/env python
from configparser import ConfigParser, ExtendedInterpolation
import logging


def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':',allow_no_value=True)  # create empty config
	cfg.optionxform = lambda option: option
	return cfg

# def set(key,value,section,file):
# 	set_key(file=file, section=section, key=key, value=value)
	
def get_config(**k):
	config=k['c']
	path=k['p']
	config.read(path)
	return config

def save_to_file(**k):
	'''
	
	:param k: f(ile)='' c(onf)=''
	:return:
	'''
	try:
		file=k['f']
		conf=k['c']
	except KeyError:
		logging.log()
	
	with open(file, 'w') as file:
		conf.write(file)
	return

def set_key(**k):
	G=k.get('config')
	file = k.get('file')
	section=k.get('section')
	key=k.get('key')
	val=k.get('val')
	config=G[file] if G.get(file) else new()
	config[section]= G[file][section] if dict(config).get(section) else {}
	config[section][key]=str(val)
	G[file]=config
	return G


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
	for key in dct.keys():
		G=set_key(key=key,val=dct[key],section=section,file=file,config=cfg)
	return G


