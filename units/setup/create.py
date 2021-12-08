#!/usr/bin/env python

from os import environ
from btrwin.units.common import libfunc as F
from btrwin.units.common import skel
from btrwin.units import conf
import btrwin.debug as d

G=btrwin.units.conf.G()

def sys_folders(path):
	DIRS= common.skel.sys.dirs()
	F.create_dtree(DIRS['sys'],path)
	d.print('dirs created')
	skel.tpl.lnks(path)
	
	d.print('symlinks created')

	return True
sys()

