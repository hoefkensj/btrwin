#!/usr/bin/env python
from configparser import ConfigParser,ExtendedInterpolation
import os
from functools import partial
from debug import *
from . import conf_base as BASE



def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option
	print('new configparser config created')
	return cfg
	
def get_dirs(parent):
	dirs=[os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
	return dirs
	
class From: #class used as function namespace so from.subfunction is valid beats having to make a casedict for it wen subfunctions
	
	def file(file):
		print('from file')
		config=new()
		config.read(file)
		return config

	def dict(dct):
		config=new()
		for key in dct.keys():
			if isinstance(key,dict):
				subcfg=new()
				for subkey in dct[key].keys():
					subcfg[subkey]= dct[key][subkey]
				dct[key] = subcfg
			config[key] = dct[key]
		return config
	
	def sysconf(conf_sys=BASE.CONF['SYS'] ):																				# reads config from system configfile /etc/betterwin/sys.conf
		dct=To.dict(From.file(conf_sys))
		return dct

	def userconf():																			# reads the users conf from files in .config
		user_conf = {}
		sysconf=From.sysconf()
		name=sysconf['GENERAL']['name']
		conf=f'{name}.conf'
		path=os.path.join(os.getenv("HOME"),'.config/',conf)
		files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
		cfg_files=[f for f in files if f[-5:] == '.conf']
		for cfg in cfg_files:
			user_conf[cfg[:-5]] = To.dict(From.file(os.path.join(path, cfg)))
		return user_conf

class To: #subfucntion class not a real class

	def file(file,conf):																			# writes config to file
		with open(file, 'w') as file:
			conf.write(file)
		return

	def dict(conf):																				# turns config into dict
		dct={}
		for section in conf:
			dct[section]= dict(conf[section])
		return dct
	
	def sysconf(conf,conf_sys=BASE.CONF['SYS']):																			# writes config to system configfile /etc/betterwin/sys.conf
		with open(conf_sys, 'w') as file:
			conf.write(file)
		return
	
	def userconf(glob_config):
		sys=glob_config.pop('SYS', None) 															# if sys in glob conf remove it
		sysconf=From.sysconf()																		#load dict sysconf form_sysconf
		name=f'{sysconf["GENERAL"]["name"]}.conf'													# construct the name for the folder
		path=os.path.join(os.getenv("HOME"),'.config',name)											# construct the full path
		if not os.path.exists(path):
			os.makedirs(path)
		for key in glob_config.keys():
			file=os.path.join(path,f'{key}.conf')
			cfg = From.dict(glob_config[key])
			To.file(conf=cfg,file=file)
		return

def from_globconf():
	usercfg=From.userconf()
	syscfg={'SYS': From.sysconf()}
	globcfg={}
	for key in syscfg.keys():
		globcfg[key]= syscfg[key]
	for key in usercfg.keys():
		globcfg[key]= usercfg[key]
	return  globcfg
	
def debug_fromglobconf(config):
	for section in config.keys():
		print(section)
		section=config[section]
		#print(section.keys())
		#d.print('main:',section)
		if isinstance(section,dict):
			for subsection in section.keys():
				print(subsection,section[subsection])
				subsection=section[subsection]
				if isinstance(subsection,dict):
					for unit in subsection.keys():
						print(unit,subsection[unit])
						unit=subsection[unit]
						if isinstance(unit,dict):
							for key in unit.keys():
								print(key,unit[key])
		return




if __name__ == '__main__' :
	#config = From.sysconf()
	#To.userconf(glob_dict)
	config=from_globconf()
	print(BASE.CONF['SYS'])
	print(config)
	print(config['SYS'])