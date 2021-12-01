#!/usr/bin/env python
import click as C
from units import fs

@C.group()
def cli():
	"""btrwin  helkp"""
@cli.group()
def fs():
	"""fs help"""
	pass
#################
@fs.group()
def btrfs():
	"""btffs help"""
	pass
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


#################
@cli.group()
def conf():
	"""conf help"""
	pass
@conf.group()
def ctl():
	"""conf help"""
	pass
@conf.group()
def pfx():
	"""conf help"""
	pass
@conf.group()
def init():
	"""conf help"""
	pass
#################


#################
@cli.group()
def prefix():
	"""prefix help"""
	pass
@prefix.group()
def loader():
	"""prefix help"""
	pass
@prefix.group()
def meta():
	"""prefix help"""
	pass
@meta.group()
def bin():
	"""bin help"""
	pass
@meta.group()
def exec():
	"""exec help"""
	pass



@prefix.group()
def template():
	"""prefix help"""
	pass
	
####################################################################################




		