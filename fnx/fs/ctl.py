#!/usr/bin/env python
import btrwin.fnx
import btrwin.lib


def check_selected_disk(disks):
	sel=btrwin.fnx.fs.selected_disk()
	if sel:
		for idx,disk in enumerate(disks):
			if disk[1]==sel:
				disks[idx][-1]= f'{disk[-1]} \033[32m*\033[0m'
	return disks

def list():
	disks= btrwin.fnx.fs.btrfs.mklist_btrfsdisks()
	disks= check_selected_disk(disks)
	btrwin.lib.func.sprint(disks, 1, 2, rownr=True, table=True)

def get_list():
	disks=btrwin.fnx.fs.btrfs.mklist_btrfsdisks()
	return  disks


