#!/usr/bin/env python
import colorama 		as color
import btrwin.lib 	as lib
import btrwin.units as units

G=units.conf.load
S=units.conf.save
lib_fsbtrfs= libH4K.lib.fs.fs_btrfs
def select_disk(idx):
	G=units.conf.load
	S=units.conf.save
	idx= idx-1
	disks = lib.fs.ls_disks('btrfs')
	G=G()
	G['btrwin']['PATH']['mount']=disks[idx][0]
	S=units.conf.save
	
def selected_disk():
	G=units.conf.load
	S=units.conf.save
	G=G()
	try:	disk = G['btrwin']['PATH']['mount']
	except KeyError: disk=None
	return disk


def mklist_btrfsdisks():
	disks = lib.fs.ls_disks('btrfs')
	selected= selected_disk()
	if any([selected in disk for disk in disks]):
		for idx,disk in enumerate(disks):
			if disk[0]==selected:
				disks[idx][-1]+=f'{color.Fore.GREEN} *{color.Style.RESET_ALL}'
	header=['Idx','Device','mountpoint','Label']
	return disks