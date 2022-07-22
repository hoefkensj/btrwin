#!/usr/bin/env python
import os
import lib

def heroic():
	tools={}
	ROOT_DIR = os.path.dirname(os.path.abspath("requirements.txt"))
	conf_ldrpaths= modules.conf.load.ctl.config(os.path.join(ROOT_DIR, 'assets/static/paths_loaders.lib'))
	loaders_wine=conf_ldrpaths['HEROIC']['WINE']
	runners=lib.fs.ls_dirs('loaders_wine')
	for runner in runners:
		tools[runner]=list_loaders(os.path.abspath(runner))
	return tools


def list_loaders(path_runner):
	runner=os.path.split(path_runner)[1]
	loaders=lib.fs.ls_dirs(path_runner)
	return loaders
	
heroic=heroic()
print(heroic)
for item in heroic:
	print(item)
	for loader in heroic[item]:
		print(loader)