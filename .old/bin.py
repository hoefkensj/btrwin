#!/usr/bin/env python
import os
import subprocess
import sys
import click_spinner
from configparser import ConfigParser,ExtendedInterpolation
##########################cfg_start
EXEC=	''
PFX=	'Epic'
##########################cfg_stop

bin=['winepath','wine64','wine','wineboot','winecfg','wineconsole','notepad','msiexec','wineserver','regsvr32','regedit',]
env=['WINEDEBUG','WINEARCH','WINEDLLOVERRIDES','WINEPREFIX','WINELOADER','WINESERVER']
# class confctl:
#
# 	def new():
# 		cfg = ConfigParser(interpolation=ExtendedInterpolation(), delimiters=':')  # create empty config
# 		cfg.optionxform = lambda option: option
# 		return cfg
#
# 	def get_dirs(parent):
# 		dirs=[os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
# 		return dirs
#
# 	def get_config(**k):
# 		config=k['config']
# 		path=k['path']
# 		config.read(path)
# 		return config
#
# 	def save_to_file(file,conf):
# 		with open(file, 'w') as file:
# 			conf.write(file)
# 		return
#
# 	def construct_global_config():
# 		glob={}
# 		files=[]
# 		path='/etc/betterwin/betterwin.conf'
# 		glob['btrwin'] = confctl.get_config(path=os.path.join(path),config=confctl.new())
# 		path=os.path.join(os.getenv("HOME"),'.config/btrwin') #=the folder ...btrwin.conf/configs..
# 		files += [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# 		cfg_files=[f for f in files if f[-5:] == '.conf']
# 		for cfg in cfg_files:
# 			glob[cfg[:-5]] = confctl.get_config(path=os.path.join(path,cfg),config=confctl.new())
# 		return glob
#
# 	def save_global_config(glob):
# 		for configfile in glob.keys():
# 			if configfile == 'btrwin':
# 				path='/etc/betterwin/betterwin.conf'
# 			else:
# 				path=os.path.join(os.getenv("HOME"),'.config/btrwin.conf',f'{configfile}.conf')
# 			config=glob[configfile]
# 			confctl.save_to_file(path,config)
#
# 	def get_global_config():
# 		return confctl.construct_global_config()
#
# 	def show_setting(**k):
# 		# for idx,configfile in enumerate(glob.keys()):
# 		# 	print(idx, '\t:\t',configfile)
# 		glob= confctl.get_global_config()
# 		if  k.get('file'):
# 			file = k['file']
# 			print(f'|->{file}/')
# 			config=glob[file]
#
# 			if k.get('section'):
# 				section=k['section']
# 				print(f'|\t|->{section}:')
#
# 				#print(config.sections())
# 				if section in config.sections():
# 					#print(glob[file][section])
# 					if 'key' in k:
# 						key=k['key']
# 						if key in config[section].keys():
# 							print(f'|\t|\t|->{key}\t:\t{glob[file][section][key]}')
# 							print()
# 						else:
# 							print('key does not exist')
# 					else:
# 						print(dict(glob[file][section]).keys())
# 				else:
# 					print('section does not exist')
# 			#print({section: dict(config[section]) for section in config.sections()})
# 			else:
# 				for section in config.sections():
# 					print(f'|\t|->[{section}]')
# 		else:
# 			print(glob.keys())
#
# 	def show_global_config():
# 		glob=confctl.get_global_config()
# 		for file in glob.keys():
# 			print(f'|---<{file}>')
# 			file=glob[file]
# 			for section in file.sections():
# 				print(f'|\t|---[{section}]')
# 				for key in dict(file[section]).keys():
# 					print(f'|\t|\t|---> {key}\t:\t{file[section][key]}')
# 				print(f'|\t|')
# 			print(f'|')
#
# 	def set_setting(**k):
# 		glob=confctl.get_global_config()
# 		file = k.get('file')
# 		section=k.get('section')
# 		key=k.get('key')
# 		val=k.get('value')
#
# 		if file:
# 			config=glob[file] if glob.get(file) else new()
# 			config[section]= glob[file][section] if dict(config).get(section) else {}
# 			config[section][key]=val
# 			glob[file]=config
# 			confctl.save_global_config(glob)
# 			return glob
#
#
# 		else :
# 			return 1 # error = 1
#
# 	def qset(key,value,section,file):
# 		confctl.set_setting(file=file,section=section,key=key,value=value)
#
# 	def set_dict(dict):
# 		file = dict.pop('file')
# 		section= dict.pop('section')
# 		for key in dict.keys():
# 			confctl.qset(key,dict[key],section,file)
# 		return

# glob= confctl.get_global_config()
# WINE_ENV=glob[PFX]['WINE_ENV']
# WINE_BIN=glob[PFX]['WINE_BIN']
#
# def main():
#
# 	global EXEC
# 	global WINE_BIN
# 	global WINE_ENV
# 	with click_spinner.spinner():
# 		b			=	{key : WINE_BIN[key.upper()] for key in bin}
# 		e			=	{**os.environ,**{key: WINE_ENV[key] for key in env}}
#
# 		args		= 	str(sys.argv[1:] if sys.argv[1:] else None)
# 		EXEC		= 	os.path.join(glob[PFX]['PATH']['ldrbin'],EXEC)
# 		EXEC		= 	f'EXEC {args}' if args else EXEC
# 		winepath	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)
# 		sserv		=	subprocess.Popen(f"{b['wineserver']} -d0 -p30",env=e,shell=True)
# 	sproc		=	subprocess.Popen(f"{b['wine']} {str(winepath.strip())[2:-1]}" ,env=e,shell=True)
# 	return sproc

# if  __name__ == '___main__':
# 	run=main()
