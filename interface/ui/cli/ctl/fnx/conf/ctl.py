#!/usr/bin/env python
import click as C
import btrwin.fnx
import btrwin.lib
import btrwin.modules.conf.load.ctl
import btrwin.modules.conf.save.ctl


@C.group()
def ctl():
	"""ctl help"""
	pass

@ctl.command()
def show():
	"""
	prints global config to stdout ;	alias for [conf] [show] [all]
	:return:
	"""
	btrwin.modules.conf.show()
	pass


@ctl.command()
@C.argument('key')
@C.argument('val')
@C.argument('section',type=str)
@C.argument('config',type=str)
def set(key,val,section,config):
	"""	\b
	set a key:value directly
	\b
	:param key: keyname to set (eg mount)
	:param val: value for that key to set
	:param section: segment in the config where the key is or will be saved: for [PATH] use PATH
	:param cfg: configfile ( the name of the config file usually the config name follews the pattern: path/to/[configname].py
	:return: None
	"""
	ctl.save_global_config(btrwin.lib.conf.set_key(key=key,val=val,section=section,file=config))
	pass

@ctl.command()
def save():
	btrwin.modules.conf.save.main.save_global_config()




@ctl.command()
def load():
	pass



@ctl.command()
def newsys():
	btrwin.modules.conf.ctl.create_new_sysconf()

