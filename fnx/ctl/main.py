#!/usr/bin/env python
import os

import btrwin.lib
import btrwin.fnx


def detect_world(name):
	world = {'config': False, 'sys': False}
	if os.path.isfile(f'/etc/btrwin/{name}.conf'):
		world['config'] = True
	if os.path.isdir(f'/opt/{name}'):
		world['sys'] = True

def create_world_config(name):
	"""
	creates the config an the configfile for the load with name
	:param name: name for the btrwinworld
	:return: the config just created
	"""
	#create the config file:
	file_world= btrwin.lib.fs.touch(f'/etc/btrwin/{name}.conf')
	#initialize the config
	conf_world=btrwin.fnx.conf.ctl.create_new_worldconf(name)
	#write the cofnig to the configfile
	btrwin.lib.conf.savefile(file=file_world, conf=conf_world)
	#read the config again from the file
	conf_world= btrwin.lib.conf.readfile(path=file_world, c=btrwin.lib.conf.new())
	#set the path of the config file in  the config now that it exists:
	conf_world['PATH']['worldconfig'] = f'{file_world}'
	#save the config again and reload
	btrwin.lib.conf.savefile(file=file_world, conf=conf_world)
	conf_world= btrwin.lib.conf.readfile(path=file_world, c=btrwin.lib.conf.new())
	return conf_world
	
def activate_world(name):
	"""
	set a load config as the active one
	:param name: name of the load config to activate
	:return: the Active World name
	"""
	os.environ["BTRWIN_WORLD_ACTIVE"]=name
	WORLD=os.environ.get('BTRWIN_WORLD_ACTIVE')
	G=btrwin.fnx.conf.load()
	return WORLD
	

def create_world_system(path,name):
	"""
	create the folder/link structure/tree  for the load with name Name
	:param path: base path upon where to create the load system
	:param name: namme of the load
	:return:
	"""
	#needs mountpoint of btrfs vol
	#needs path to the load base dir opt/btrwin | opt/load
	#a load config must exist

	# dirs	=	assets.skel.skels.SKELLS['SYS']['DIRS']
	# links	=	assets.skel.skels.SKELLS['SYS']['LINKS']
	# lib.fs.mkdirtree(dirs['sys'], path)
	
	# def sys_links(**k):
	#
	# 	lib.fs.mklinktree(links, **k)


def select_disk(id):
	"""
	select btrfs volume to use for the active load
	:param id: id of the btrfs volume
	:return:
	"""
	valid = detect_disk()
	if id  in range(1, valid + 1):
		btrwin.fnx.fs.select_disk(id)
		done=True
	else:
		done=False
	return done

def detect_disk():
		valid = 0
		for idx, dsk in enumerate(btrwin.lib.fs.ls_blockdev('btrfs')):
			valid = idx + 1
		return valid
		
def default_disk():
	return [idx + 1 for idx, dsk in enumerate(btrwin.lib.fs.ls_blockdev('btrfs')) if btrwin.fnx.fs.selected_disk() in dsk[1]]
	
def setup_sys(mount, pth):
	USERHOME = os.environ.get('HOME')
	USER = os.environ.get('USER')
	PATH = os.path.join(mount, pth)
	btrwin.fnx.file.create.ctl.sys_folders(PATH)
	btrwin.fnx.file.create.ctl.sys_links(USERHOME=USERHOME, USER=USER, PATH=PATH)
	
