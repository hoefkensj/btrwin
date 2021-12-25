#!/usr/bin/env python
import click as C



@C.group()
def btrfs():
	"""btrtfs help"""
	pass
	#################





@btrfs.command()
def create(parent,name):
	"""create new btrfs subvolume"""
	fs.btrfs.create_subv(parent,name)
	pass
@btrfs.command()
def delete():
	"""delete btrfs subvolume"""
	pass
@btrfs.command()
def snapshot():
	"""duplicate btrfs subvolume"""
	pass
@btrfs.command()
def list():
	"""list  btrfs subvolumes"""
	pass
@btrfs.command()
def ids():
	"""create identifiers in the  btrfs subvolume"""
	pass
#################
