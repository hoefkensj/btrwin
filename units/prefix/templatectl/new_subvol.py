#!/usr/bin/env python
import btrwin.units as units
import btrwin.lib as lib
import debug as d
import os

fs=lib.fs_btrfs
def new_subvol():

	before		= fs.get_subvs(dir_subv)
	name 		= tpl_name(exist=before,bit=settings['bit'],subv=dir_subv)

	fs.create_subv(dir_subv, name)
	dir_tpl		= os.path.join(dir_subv,name)
	after		= fs.get_subvs(dir_subv)
	diff 		= [subv for subv in after if subv not in before][0]
	if diff == dir_tpl :
		d.print('successfully created subvolume', name)
		return name
	#TODO write settings to meta/etc/
	#Todo write settings to ~/.config/?/tplname
	return False