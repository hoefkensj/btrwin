#!/usr/bin/env python
import click as C
import btrwin.fnx.conf.load.ctl

@C.group()
def load():
	pass

@load.command()
def env():
	btrwin.fnx.conf.load.ctl.env_config()

@load.command()
def rc():
	btrwin.fnx.conf.load.ctl.running_config()

@load.command()
def loaduser():
	btrwin.fnx.conf.load.ctl.user_configs()

@load.command()
def loadsys():
	btrwin.fnx.conf.load.ctl.sys_config()

