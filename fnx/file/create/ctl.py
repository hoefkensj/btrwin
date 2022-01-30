#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import btrwin.fnx
import btrwin.assets
import btrwin.lib


def create_world_system(path,name):
	"""
	create the folder/link structure/tree  for the load with name Name
	:param path: base path upon where to create the load system
	:param name: namme of the load
	:return:
	"""
	#needs mountpoint of btrfs vol
	#needs path to the load base dir opt/btrwin | opt/load
	#a load config must exist
	G=btrwin.fnx.conf.load()
	for iet in G:
		print(iet)
def sys_folders(path):
	dirs= btrwin.assets.static.skel.skels.SKELLS['SYS']['DIRS']
	btrwin.lib.fs.mkdirtree(dirs['sys'], path)
def sys_links(**k):
	links= btrwin.assets.static.skel.skels.SKELLS['SYS']['LINKS']
	btrwin.lib.fs.mklinktree(links, **k)