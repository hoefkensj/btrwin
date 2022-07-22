#!/usr/bin/env python
import click as C
import btrwin.modules.conf.load.ctl

@C.group()
def load():
	pass

@load.command()
def env():
	btrwin.modules.conf.load.ctl.env_config()

@load.command()
def rc():
	btrwin.modules.conf.load.ctl.running_config()

@load.command()
def loaduser():
	btrwin.modules.conf.load.ctl.user_configs()

@load.command()
def loadsys():
	btrwin.modules.conf.load.ctl.sys_config()

