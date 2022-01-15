#!/usr/bin/env python
print('import os,platform,sys')
import os,platform,sys
print('from btrwin import btrwin as main')
from btrwin import btrwin as main



def Linux():
		main.cli()
def Windows():
	print('Sorry the Windows Part of this software is still under development and hasnt been implemented yet in this version of the software...\n exiting...')
	exit()
def select_platform(this_platform=None):
	
	platform_systems={
		'Linux' : Linux,
		'Windows': Windows,
	}
	if platform.platform:
		this_platform=platform_systems[platform.system()]
	return this_platform

if __name__ == '__main__':
	this_platform =	select_platform()
	if any([True for flag  in sys.argv if flag == '--debug']) or any([True for flag  in sys.argv if flag == '-D']):
		print('Debug flag found, running Linux version of the software in WindowsNT mode:')
		this_platform=Linux

	this_platform()
