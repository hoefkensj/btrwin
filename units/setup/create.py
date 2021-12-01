#!/usr/bin/env python

from os import environ
from .. import common
from units.common import libfunc as F
import debug as d


def sys(path):

	DIRS= common.skel.sys.dirs()
	F.create_dtree(DIRS['sys'],path)
	d.print('dirs created')
	common.skel.tpl.lnks(path=path)
	d.print('symlinks created')
	#link wine to /loader
	#populate /meta/bin
	#
	return True

