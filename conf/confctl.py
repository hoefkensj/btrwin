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
	
def from_file(file):
	config=new()
	config.read(file)
	return config

def from_dict(dct):
	config=new()
	for key in dct.keys():
		if isinstance(key,dict):
			subcfg=new()
			for subkey in dct[key].keys():
				subcfg[subkey]= dct[key][subkey]
			dct[key] = subcfg
		config[key] = dct[key]
	return config
	
def from_sysconf():
	dct=to_dict(from_file('/etc/betterwin/sys.conf'))
	return dct

def from_userconf():
	user_conf = {}
	sysconf=from_sysconf()
	name=sysconf['GENERAL']['name']
	conf=f'{name}.conf'
	path=os.path.join(os.getenv("HOME"),'.config',conf)
	files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	cfg_files=[f for f in files if f[-5:] == '.conf']
	for cfg in cfg_files:
		user_conf[cfg[:-5]] = to_dict(from_file(os.path.join(path, cfg)))
	return user_conf

def to_file(file,conf):
	with open(file, 'w') as file:
		conf.write(file)
	return

def to_dict(conf):
	dct={}
	for section in conf:
		dct[section]= dict(conf[section])
	return dct

def to_sysconf(conf):
	with open('/etc/betterwin/sys.conf', 'w') as file:
		conf.write(file)
	return

def to_userconf(glob_config):
	sys=glob_config.pop('SYS', None) 															# if sys in glob conf remove it
	sysconf=from_sysconf()																		#load dict sysconf form_sysconf
	name=f'{sysconf["GENERAL"]["name"]}.conf'													# construct the name for the folder
	path=os.path.join(os.getenv("HOME"),'.config',name)											# construct the full path
	if not os.path.exists(path):
		os.makedirs(path)
	for key in glob_config.keys():
		file=os.path.join(path,f'{key}.conf')
		cfg = from_dict(glob_config[key])
		to_file(conf=cfg,file=file)
	return

def from_globconf():
	usercfg=from_userconf()
	syscfg= from_sysconf()
	globcfg=usercfg
	globcfg['SYS']=syscfg
	return  globcfg
	

if __name__ == '__main__' :
	#config = from_sysconf()
	#to_userconf(glob_dict)

	config=from_globconf()
	for section in config.keys():
		print(section,config[section].keys())
