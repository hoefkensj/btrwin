#!/usr/bin/env python
import os,btrfsutil
def get_dirs(parent):
	return [os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]

def get_subvs(parent):
	subvs=[]
	list=get_dirs('/mnt/btrd0v1/opt/BTRWin/subv')
	for dir in list:
		if btrfsutil.is_subvolume(dir):
		
		# ino=os.stat(dir).st_ino
		#
		# if ino == 256:
			subvs +=[dir]
	return subvs
		
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
	created=btrfsutil.create_subvolume(subv)
	add_idfiers(subv)
	return created
	
def del_subv(parent,name):
	subv=os.path.join(parent, name)
	deleted=btrfsutil.delete_subvolume(subv)
	return deleted


