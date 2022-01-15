#!/usr/bin/env python
import logging
import colorama

import btrwin.lib 		as lib
import btrwin.units 	as units


def check_selected_disk(disks):
	sel=units.fs.selected_disk()
	if sel:
		for idx,disk in enumerate(disks):
			if disk[1]==sel:
				disks[idx][-1]= f'{disk[-1]} {colorama.Fore.GREEN} *{colorama.Style.RESET_ALL}'
	return disks

def list():
	disks= units.fs.btrfs.mklist_btrfsdisks()
	disks= check_selected_disk(disks)
	lib.func.sprint(disks, 1, 2, rownr=True, table=True)

def get_list():
	disks=units.fs.btrfs.mklist_btrfsdisks()
	return  disks


