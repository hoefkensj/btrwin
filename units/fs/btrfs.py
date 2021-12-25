#!/usr/bin/env python
import btrwin.lib as lib
import btrwin.units as units
import colorama as style



G=units.conf.load()
S=units.conf.save

def select_disk(idx):
	idx= idx-1
	disks = lib.fs.ls_disks('btrfs')
	G=units.conf.load()
	G['btrwin']['PATH']['mount']=disks[idx][0]
	G=S(G)
	
def selected_disk():
	G=units.conf.load()
	try:	disk = G['btrwin']['PATH']['mount']
	except KeyError: disk=None
	return disk


def mklist_btrfsdisks():
	disks = lib.fs.ls_disks('btrfs')
	selected= selected_disk()
	if any([selected in disk for disk in disks]):
		for idx,disk in enumerate(disks):
			if disk[0]==selected:
				disks[idx][-1]+=f'{style.Fore.GREEN} *{style.Style.RESET_ALL}'
	header=['Idx','Device','mountpoint','Label']
	return disks