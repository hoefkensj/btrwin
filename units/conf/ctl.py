#!/usr/bin/env python
import os

import btrwin.lib.fs as lib_fs
from btrwin.lib.conf import new, get_config, save_to_file

pjoin=os.path.join


def get_user_config(user,cfg):
	get_config(p=pjoin(user, f'{cfg}.conf'), c=new())

def get_global_config(path_sysconf='/etc/btrwin/btrwin.conf',path_userconfig='.config/btrwin'):
	sys=path_sysconf
	user=os.path.join(os.getenv("HOME"),path_userconfig) #=the folder ...btrwin.conf/configs..
	files = lib_fs.ls_files(user)
	cfg_files=[os.path.split(f)[1][:-5] for f in files if f[-5:] == '.conf']
	glob= {'btrwin' : get_config(p=pjoin(sys), c=new())}
	for cfg in cfg_files:
		glob[cfg] = get_config(p=pjoin(user, f'{cfg}.conf'), c=new())
	return glob

def save_global_config(G):

	for configfile in G.keys():
		if configfile == 'btrwin':
			path='/etc/btrwin/btrwin.conf'
		else:
			path=os.path.join(os.getenv("HOME"),'.config/btrwin',f'{configfile}.conf')
		config=G[configfile]
		save_to_file(path, config)

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

def create_new_sysconf(fname):
	if not '/etc/btrwin' in lib_fs.ls_dirs('/etc/'):
		os.mkdir('/etc/btrwin')

	lib_fs.touch(f'/etc/btrwin/{fname}.conf')
	with open(f'/etc/btrwin/{fname}.conf','w') as f:
				f.write(f'[PATH]\nsysconfig\t:\t/etc/btrwin/{fname}.conf\n[ORG]\nNAME\t:\t{fname}')

