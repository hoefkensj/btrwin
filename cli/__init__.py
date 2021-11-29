#!/usr/bin/env python
import click as C
import betterwin as B
from betterwin.fs import btrfs

@C.group()
def cli():
	'''betterwin  helkp'''
@cli.group()
def fs():
	'''fs help'''
	pass
############################################################
@fs.group()
def btrfs():
	'''btffs help'''
	pass

@btrfs.command()
def create():
	'''create new btrfs subvolume'''
	pass
@btrfs.command()
def delete():
	'''delete btrfs subvolume'''
	pass
@btrfs.command()
def snapshot():
	'''duplicate btrfs subvolume'''
	pass
@btrfs.command()
def list():
	'''list  btrfs subvolumes'''
	pass
@btrfs.command()
def ids():
	'''create identifiers in the  btrfs subvolume'''
	pass
########################################################################



@cli.group()
def conf():
	'''conf help'''
	pass
@conf.group()
def ctl():
	'''conf help'''
	pass
@conf.group()
def pfx():
	'''conf help'''
	pass
@conf.group()
def init():
	'''conf help'''
	pass

####################################################################################
@cli.group()
def prefix():
	'''prefix help'''
	pass

@prefix.group()
def loader():
	'''prefix help'''
	pass
@prefix.group()
def meta():
	'''prefix help'''
	pass
@meta.group()
def bin():
	'''bin help'''
	pass
@meta.group()
def exec():
	'''exec help'''
	pass



@prefix.group()
def template():
	'''prefix help'''
	pass
	
####################################################################################




		