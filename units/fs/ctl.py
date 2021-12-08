#!/usr/bin/env python
import os
from os import makedirs

import subprocess_tee as sproc


def get_dirs(parent):
	return [os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]

def get_disks(type):

	result = sproc.run('lsblk -I 259,8 --list -o FSTYPE,NAME,MOUNTPOINT', tee=False)
	resultsplit = result.stdout.strip().split('\n')
	mounted=[line for line in resultsplit if any('/' in i for i in line.split())]
	vols=	[line for line in mounted if type in line ]
	vols =[[col for col in reversed(vol.split()[1:])] for vol in vols]
	return vols

def create_dtree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			makedirs(next_path)
			create_dtree(info, next_path)
	return

	
	
if __name__ == '__main__':
	get_disks('btrfs')
	