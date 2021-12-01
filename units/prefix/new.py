#!/usr/bin/env python3

from betterwin.fsctl import btrfsctl
from betterwin.confctl import confctl,glob,pfx



def create_new_prefix(NAME,TPL):
	parent=str(glob['btrwin']['PATH']['subv'])
	print(parent,NAME,TPL)
	prefix = btrfsctl.create_snapshot(parent,dst=NAME,src=TPL)
	config = pfx.create_prefix_config(NAME,TPL=TPL)


def __main__(NAME,TPL):
	create_new_prefix(NAME,TPL)

