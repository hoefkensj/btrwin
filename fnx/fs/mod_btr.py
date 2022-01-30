#!/usr/bin/env python

import os
import btrfsutil
def create_subv(parent,name):
	"""
	:param parent:
	:param name:
	:return:
	"""

	subv=os.path.join(parent, name)
	btrfsutil.create_subvolume(subv)
	install_btrfs_subv_meta(subv)
	return subv
	
def del_subv(parent,name):
	"""
	:param parent:
	:param name:
	:return:
	"""

	subv=os.path.join(parent, name)
	deleted=btrfsutil.delete_subvolume(subv)
	return deleted

def create_snapshot(parent,src,dst):
	"""
	:param parent:
	:param src:
	:param dst:
	:return:
	"""
	
	subv_src=os.path.join(parent, src)
	subv_dst=os.path.join(parent, dst)
	btrfsutil.create_snapshot(subv_src,subv_dst)
	return

def get_subvs(parent):
	"""
	:param parent:
	:return:
	"""
	
	#ls_dirs=[os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
	return [directory for directory in os.listdir(parent) if btrfsutil.is_subvolume(directory)]

def install_btrfs_subv_meta(subv):
	"""
	:param subv:
	:return:
	"""
	ini=os.path.join(subv, 'desktop.ini')
	dot=os.path.join(subv, '.directory')
	bang=os.path.join(subv, f'.!{subv.split("/")[-1].upper()}!.')
	with open(ini, 'w') as file:
		contents=f'[.ShellClassInfo]\r\nIconResource=C:\Windows\System32\SHELL32.dll,7'
		file.write(contents)
	with open(dot, 'w') as file:
		contents=f'[Desktop Entry]\nIcon=drive-partition'
		file.write(contents)
	with open(bang, 'w') as file:
		contents=f'# {subv.split("/")[-1].upper()}\n[Desktop Entry]\nIcon=drive-partition'
		file.write(contents)
