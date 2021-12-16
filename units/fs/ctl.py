#!/usr/bin/env python
import logging
import btrwin.lib as lib
import btrwin.units.fs as fs
from colorama import Style,Fore

def check_selected_disk(disks):
	sel=fs.selected_disk()
	if sel:
		for idx,disk in enumerate(disks):
			if disk[1]==sel:
				disks[idx][-1]= f'{disk[-1]} {Fore.GREEN} *{Style.RESET_ALL}'
	return disks

def list():
	disks= fs.btrfs.mklist_btrfsdisks()
	disks= check_selected_disk(disks)
	lib.func.sprint(disks, 1, 2, rownr=True, table=True)

def get_list():
	disks=fs.btrfs.mklist_btrfsdisks()
	return  disks


