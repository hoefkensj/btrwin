#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import os

import btrwin.lib
def check_inst(name):
		G=fnx.conf.load
		G=G()
		exist_cfg= True if os.path.exists('/etc/btrwin/{name}.conf') else False
		exist_keyval= True if dict(G['btrwin']['PATH']).get('mount') else False
		return exist_cfg and exist_keyval

def sysconfig_folder():
	#check for existing folder btrwin in /etc and in ~/.config
	sys = True if 'btrwin' in [os.path.split(dir)[1] for dir in btrwin.lib.fs.ls_dirs('/etc')] else False
	return sys

def userconfig_folder(name):
	user= True if name in btrwin.lib.fs.ls_dirs('~/.config') else False
	return user

def detect_world(name):
	world = {'config': False, 'sys': False}
	if os.path.isfile(f'/etc/btrwin/{name}.conf'):
		world['config'] = True
	if os.path.isdir(f'/opt/{name}'):
		world['sys'] = True

def detect_disk():
		valid = 0
		for idx, dsk in enumerate(btrwin.lib.fs.ls_blockdev('btrfs')):
			valid = idx + 1
		return valid

def detect_loaders_wine(path):
	dirs=btrwin.lib.fs.ls_dirs(path)
	installed_loaders=[os.path.split(dir)[1] for dir in dirs]
	installed_paths=dirs
	installed={}
	for idx,loader in enumerate(installed_loaders):
		installed[loader]={}
		installed[loader]['NAME']=loader
		installed[loader]['PATH']=installed_paths[idx]
	return installed