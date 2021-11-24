#!/usr/bin/env python3
"""Hello World implementation using MILC.

PYTHON_ARGCOMPLETE_OK
"""

from milc import cli
from betterwin.fsctl import btrfsctl
from betterwin.confctl import confctl,glob,pfx
import milc.subcommand.config


def create_new_prefix(NAME,TPL):
	parent=str(glob['betterwin']['PATH']['subv'])
	print(parent,NAME,TPL)
	prefix = btrfsctl.create_snapshot(parent,dst=NAME,src=TPL)
	config = pfx.create_prefix_config(NAME,TPL=TPL)



