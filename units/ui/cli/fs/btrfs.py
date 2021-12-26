#!/usr/bin/env python
import click as C
import btrwin.units as units



@C.group()
def btrfs():
	"""btrtfs help"""
	pass


@btrfs.command()
@C.argument('-p','--parent')
@C.argument('-n','--name')
def create(parent,name):
	"""
	create new subvolume with [name] in [parent]
	:param parent:
	:param name:
	:return:
	"""
	units.fs.btrfs.lib_fsbtrfs.create_subv(parent,name)
	pass
	
@btrfs.command()
@C.argument('-p','--parent')
@C.argument('-n','--name')
def delete(parent,name):
	"""
	delete btrfs subvolume
	:param parent:
	:param name:
	:return:
	"""
	units.fs.btrfs.lib_fsbtrfs.del_subv(parent=parent,name=name)
	pass
	
@btrfs.command()
@C.argument('-p','--parent')
@C.argument('-s','--source')
@C.argument('-n','--name')
def snapshot(parent,source,name):
	"""
	duplicate btrfs subvolume"
	:param parent:
	:param source:
	:param name:
	:return:
	"""
	units.fs.btrfs.lib_fsbtrfs.create_snapshot(parent=parent,src=source,dst=name)
	pass

@btrfs.command()
def list():
	"""
	list  btrfs subvolumes
	:return:
	"""

	pass

@btrfs.command()
@C.argument('-s','--sub','--subvolume')
def ids(subvolume):
	"""
	create identifiers in the  btrfs subvolume
	:param subvolume:
	:return:
	"""
	units.fs.btrfs.lib_fsbtrfs.add_idfiers(subv=subvolume)
	pass

