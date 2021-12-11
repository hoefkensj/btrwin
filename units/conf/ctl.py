#!/usr/bin/env python
from configparser import ConfigParser,ExtendedInterpolation
import os
from btrwin.units.common import ls_dirs,ls_files

pjoin=os.path.join

def new():
	cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
	cfg.optionxform = lambda option: option
	return cfg
	
def get_config(**k):
	config=k['c']
	path=k['p']
	config.read(path)
	return config
	
def save_to_file(file,conf):
	with open(file, 'w') as file:
		conf.write(file)
	return
	
def get_user_config(user,cfg):
	get_config(p=pjoin(user,f'{cfg}.conf'),c=new())

def construct_global_config(path_sysconf='/etc/btrwin/btrwin.conf',path_userconfig='.config/btrwin'):
	sys=path_sysconf
	user=os.path.join(os.getenv("HOME"),path_userconfig) #=the folder ...btrwin.conf/configs..
	files = ls_files(user)
	cfg_files=[os.path.split(f)[1][:-5] for f in files if f[-5:] == '.conf']
	glob= {'btrwin' : get_config(p=pjoin(sys),c=new())}
	for cfg in cfg_files:
		glob[cfg] = get_config(p=pjoin(user,f'{cfg}.conf'),c=new())
	return glob

def save_global_config(G):
	loc_sys=G['btrwin']['PATH']['config']
	for configfile in G.keys():
		if configfile == 'btrwin':
			path='/etc/btrwin/btrwin.conf'
		else:
			path=os.path.join(os.getenv("HOME"),'.config/btrwin.conf',f'{configfile}.conf')
		config=G[configfile]
		save_to_file(path,config)

def set_key(**k):
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

def set_dict(dct):
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
	[set_key(key=key,val=dict[key],section=section,file=file) for key in dct.keys()]


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
				if divmod(len(key),2)[0] >= tabs:
					print(f'|\t|\t|---> {key}',' ',f':\t{file[section][key]}')
				elif divmod(len(key),2)[0] == tabs-1:
					print(f'|\t|\t|---> {key}','\t',f':\t{file[section][key]}')
				elif divmod(len(key),2)[0] <= (tabs-2):
					print(f'|\t|\t|---> {key}','\t',f':\t{file[section][key]}')
			print(f'|\t|')
		print(f'|')
