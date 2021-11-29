#!/usr/bin/env python
import os,subprocess
import subprocess_tee as sproc
def get_dirs(parent):
	return [os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]

def get_disks():
	result = sproc.run('lsblk -I 259,8 --list -o FSTYPE,LABEL,PARTLABEL,NAME', tee=False)
	resultsplit = result.stdout.strip().split('\n')
	for line in resultsplit:
		if 'btrfs' in line:
			print(line)
	
	
if __name__ == '__main__':
	get_disks()