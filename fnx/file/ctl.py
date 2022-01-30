#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import os

import btrwin.fnx.file
import btrwin.fnx.fs
import btrwin.lib
def default_disk():
	return [idx + 1 for idx, dsk in enumerate(btrwin.lib.fs.ls_blockdev('btrfs')) if btrwin.fnx.fs.selected_disk() in dsk[1]]
def setup_sys(mount, pth):
	USERHOME = os.environ.get('HOME')
	USER = os.environ.get('USER')
	PATH = os.path.join(mount, pth)
	btrwin.fnx.file.create.ctl.sys_folders(PATH)
	btrwin.fnx.file.create.ctl.sys_links(USERHOME=USERHOME, USER=USER, PATH=PATH)