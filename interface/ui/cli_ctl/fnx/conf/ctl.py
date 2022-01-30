#!/usr/bin/env python
import click as C
import btrwin.fnx
import btrwin.lib
import btrwin.fnx.conf.load.ctl
import btrwin.fnx.conf.save.ctl
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
	btrwin.fnx.conf.show()
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
	btrwin.fnx.conf.save.main.save_global_config()

@ctl.command()
def loadenv():
	btrwin.fnx.conf.load.main.load_env_config()

@ctl.command()
def loaduser():
	btrwin.fnx.conf.load.main.load_user_configs()

@ctl.command()
def loadsys():
	btrwin.fnx.conf.load.main.load_sys_config()

@ctl.command()
def newsys():
	btrwin.fnx.conf.ctl.create_new_sysconf()

