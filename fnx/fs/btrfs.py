#!/usr/bin/env python

import btrwin.fnx
import btrwin.lib

def select_disk(**k):
	G=btrwin.fnx.conf.load.ctl.load_world_config()
	idx=k.get('idx')
	disks = btrwin.lib.fs.ls_blockdev()
	G['btrwin']['PATH']['mount']=disks[idx][0]
	

	
def selected_disk():
	G=btrwin.fnx.conf.load.ctl.load_global_config()
	try:	disk = G['btrwin']['PATH']['mount']
	except KeyError: disk=None
	return disk


def mklist_btrfsdisks():
	disks = btrwin.lib.fs.ls_fs_btrfs()
	for idx,disk in enumerate(disks):
		disks[idx]=disk
		
	selected= selected_disk()
	if any(str(selected) in disk for disk in disks):
		for idx,disk in enumerate(disks):
			if disk[0]==selected:
				disks[idx][-1] += '\x1b[32m *\x1b[0m'
	header=['Idx','Device','Label','FSType']
	return disks,header



