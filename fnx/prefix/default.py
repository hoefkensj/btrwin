#!/usr/bin/env python
#sets the default prefix for ~/.winm
import sys,os
import fnx as units

def get_pfxx()
	subvs=fnx.fs.btrfs.get_subvs()
	pfxx=[pfx for pfx in subvs if 'tpl'  not in pfx]
	return pfxx

def rmwinehome():
	sys.path.remove('~/.wine')
	return

def lnpfx(src):
	pfxx=get_pfxx()
	src=[pfx for pfx in pfxx if pfx == src]
	if src is not None:
		rmwinehome()
		os.symlink(src,'~/.wine')
