#!/usr/bin/env python

from os import environ
from btrwin.units.fs import ctl
from btrwin.units.conf import G
from btrwin.units.common import libfunc
G=G()

def select():
 pass


def list():
	disks = ctl.get_disks('btrfs')
	libfunc.sprint_table(disks,2,4,rownr=True)
		




if __name__ == '__main__':
	list()