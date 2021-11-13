#!/usr/bin/env python
from configparser import ConfigParser,ExtendedInterpolation
import os

defaultdct= {
	'key1' : 'val1',
	'key2'	: 'val2'
			}
testingdct= {
	'keya' : '${key1}vala',
	'keyb'	: 'valb'
			}
testdct= {
		'DEFAULT' : defaultdct,
		'testing' : testingdct
}
glob_dict= { 'file1' : testdct}

def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option

	return cfg
	
def from_file(file):
	config=new()
	config.read(file)
	return config

def from_dict(dct):
	config=new()
	for key in dct.keys():
		if isinstance(key,dict):
			section=key
			subcfg=new()
			subdct = dct[key]
			for subkey in subdct.keys():
				subcfg[subkey]= subdct[subkey]
			dct[key] = subcfg
		config[key] = dct[key]
	return config
	
def to_file(file,conf):
	with open(file, 'w') as file:
		conf.write(file)
	return

def to_dict(conf):
	dct={}
	for section in conf:
		dct[section]= dict(conf[section])
	return dct

def get_dirs(parent):
	return [os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
	
	
def from_sysconf():
	conf=from_file('/etc/betterwin/sys.conf')
	dct=to_dict(conf)
	return dct

def to_userconf(glob_config):
	sys=glob_config.pop('SYS', None)
	sysconf=from_sysconf()
	name=f'{sysconf["GENERAL"]["name"]}.conf'
	path=os.path.join(os.getenv("HOME"),'.config',name)
	print(path)
	if not os.path.exists(path):
		os.makedirs(path)
	for key in glob_config.keys():
		conffile=f'{key}.conf'
		file=os.path.join(path,conffile)
		cfg = from_dict(glob_config[key])
		to_file(conf=cfg,file=file)
	return

def from_userconf():
	def get_userconfig(betterwin):
		conf=f'{betterwin}.conf'
		userconf={}
		path=os.path.join(os.getenv("HOME"),'.config',conf)
		if os.path.isdir(path):
			userconf=get_multiconf(path)
		elif os.path.isfile(path):
			userconf=from_file(path)
		return userconf
		
	def get_multiconf(parent):
		files = [f for f in os.listdir(parent) if os.path.isfile(os.path.join(parent, f))]
		user_conf = {}
		cfg_files=[]
		for file in files :
			if file[-5:] == '.conf':
				cfg_files.extend(file)
		for cfg in cfg_files:
			path=os.path.join(parent, cfg)
			conf=from_file(path)
			dct=to_dict(conf)
			user_conf[cfg[:-5]]=dct
		return user_conf
		
	sysconf=from_sysconf()
	name=sysconf['GENERAL']['name']
	glob_conf=get_userconfig(name)
	return glob_conf
	


if __name__ == '__main__' :
	#config = from_sysconf()
	to_userconf(glob_dict)
	config=from_userconf()
	for section in config.keys():
		print(section,config[section])
		