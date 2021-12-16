#!/usr/bin/env python
import os

import lib.fs
from btrwin.units import fs


def sysconfig_folder():
	#check for existing folder btrwin in /etc and in ~/.config
	sys = True if 'btrwin' in [os.path.split(dir)[1] for dir in lib.fs.ls_dirs('/etc')] else False
	return sys

def userconfig_folder(name):
	user= True if name in lib.fs.ls_dirs('~/.config') else False
	return user

def main():
	print(sysconfig_folder())

if __name__ == '__main__':
	main()
