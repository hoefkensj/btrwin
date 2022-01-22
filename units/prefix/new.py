#!/usr/bin/env python3

import btrwin.units as units

from betterwin.fsctl import
btrfsctl
from betterwin.confctl import
 confctl,glob,pfx

libH4K.lib.fs.fs_btrfs.

def create_new_prefix(NAME,TPL):
	parent=str(glob['btrwin']['PATH']['subv'])
	print(parent,NAME,TPL)
	prefix = libH4K.lib.fs.fs_btrfs.create_snapshot(parent, dst=NAME, src=TPL)
	config = units.prefix.new.create_prefix_config(NAME,TPL=TPL)


def __main__(NAME,TPL):
	create_new_prefix(NAME,TPL)

