#!/usr/bin/env python

def create_subv(parent,name):
	import btrfsutil
	import os
	subv=os.path.join(parent, name)
	btrfsutil.create_subvolume(subv)
	add_idfiers(subv)
	return subv
	
def del_subv(parent,name):
	import btrfsutil
	import os
	subv=os.path.join(parent, name)
	deleted=btrfsutil.delete_subvolume(subv)
	return deleted

def create_snapshot(parent,src,dst):
	import btrfsutil
	import os
	subv_src=os.path.join(parent, src)
	subv_dst=os.path.join(parent, dst)
	btrfsutil.create_snapshot(subv_src,subv_dst)
	return

def get_subvs(parent):
	import btrfsutil
	from btrwin.lib.fs import ls_dirs
	return [directory for directory in ls_dirs(parent) if btrfsutil.is_subvolume(directory)]

def add_idfiers(subv):
	import os
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
