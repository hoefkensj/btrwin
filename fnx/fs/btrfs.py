#!/usr/bin/env python

import btrwin.fnx
import btrwin.lib

def select_disk(idx):
	G=btrwin.fnx.conf.load
	idx= idx-1
	disks = btrwin.lib.fs.ls_blockdev()
	print(disks)
	G=G()
	G['btrwin']['PATH']['mount']=disks[idx][0]

	
def selected_disk():
	G=btrwin.fnx.conf.load.ctl.load_global_config()
	G=G()
	try:	disk = G['btrwin']['PATH']['mount']
	except KeyError: disk=None
	return disk


def mklist_btrfsdisks():
	disks = btrwin.lib.fs.ls_blockdev('btrfs')
	selected= selected_disk()
	if any(selected in disk for disk in disks):
		for idx,disk in enumerate(disks):
			if disk[0]==selected:
				disks[idx][-1] += '\x1b[32m *\x1b[0m'
	header=['Idx','Device','mountpoint','Label']
	return disks



