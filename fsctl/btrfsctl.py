#!/usr/bin/env python
import os,btrfsutil
from betterwin import debug as d
from betterwin.confctl import confctl
from betterwin.fsctl import fsctl

def get_subvs(parent):
	return [dir for dir in fsctl.get_dirs(parent) if btrfsutil.is_subvolume(dir)]

		
def add_idfiers(subv):
	ini=os.path.join(subv, 'desktop.ini')
	dot=os.path.join(subv, '.directory')
	with open(ini, 'w') as file:
		contents=f'[.ShellClassInfo]\r\nIconResource=C:\Windows\System32\SHELL32.dll,7'
		file.write(contents)
	with open(dot, 'w') as file:
		contents=f'[Desktop Entry]\nIcon=drive-partition'
		file.write(contents)
	
def create_subv(parent,name):
	subv=os.path.join(parent, name)
	btrfsutil.create_subvolume(subv)
	add_idfiers(subv)
	return subv
	
def del_subv(parent,name):
	subv=os.path.join(parent, name)
	deleted=btrfsutil.delete_subvolume(subv)
	return deleted


def create_snapshot(parent,src,dst):
	subv_src=os.path.join(parent, src)
	subv_dst=os.path.join(parent, dst)
	btrfsutil.create_snapshot(subv_src,subv_dst)
	return