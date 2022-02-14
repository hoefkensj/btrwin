#!/usr/bin/env python
import btrwin.fnx.fs.btrfs
import btrwin.lib.func

def check_selected_disk(disks):
	sel=btrwin.fnx.fs.btrfs.selected_disk()
	if sel:
		for idx,disk in enumerate(disks):
			if disk[1]==sel:
				disks[idx][-1]= f'{disk[-1]} \033[32m*\033[0m'
	return disks

def list():
	disks= btrwin.fnx.fs.btrfs.mklist_btrfsdisks()
	disks= check_selected_disk(disks)
	btrwin.lib.func.sprint(disks[0], 1, 2, rownr=True, table=True)

def get_list():
	disks=btrwin.fnx.fs.btrfs.mklist_btrfsdisks()
	return  disks

def fs_select_set(id):
	"""
	select btrfs volume to use for the active load
	:param id: id of the btrfs volume
	:return:
	"""
	valid = fnx.check.ctl.detect_disk()
	if id  in range(1, valid + 1):
		btrwin.fnx.fs.select_disk(id)
		done=True
	else:
		done=False
	return done