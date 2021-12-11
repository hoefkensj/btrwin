#!/usr/bin/env python
from os import makedirs
from btrwin import G,S
from btrwin.units.common import libfunc
import subprocess_tee as sproc
from btrwin import  debug as d

G=G()

def get_disks(type):
	split=[]
	result = sproc.run("lsblk -I 259,8 --list -o FSTYPE,PATH,MOUNTPOINT,LABEL |awk '$1==\"btrfs\" {print $2,$4,$3}'| awk '$3 != \"\" {print $1, $3,$2 }'", tee=False)
	resultsplit = result.stdout.strip().split('\n')
	for line in resultsplit:
		split+=[line.split()]
	return split

def create_directory_tree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			makedirs(next_path)
			create_directory_tree(info, next_path)

def select(idx):
	idx= idx-1
	disks = get_disks('btrfs')
	G['btrwin']['PATH']['mount']=disks[idx][0]
	S(G)


def list():
	disks = get_disks('btrfs')
	selected= G['btrwin']['PATH']['mount']
	if any([selected in disk for disk in disks]):
		for idx,disk in enumerate(disks):
			if disk[0]==selected:
				disks[idx][-1]+=f'*'
	header=['Idx','Device','mountpoint','Label']

	libfunc.sprint_table(disks,1,2,rownr=True)