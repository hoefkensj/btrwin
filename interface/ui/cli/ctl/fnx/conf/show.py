#!/usr/bin/env python
import click as C

@C.group()
def show():
	"""btrtfs help"""

	pass
	#################

@show.command()
def all():
	"""prints full config to  stdout"""
	import btrwin.fnx.conf.ctl
	btrwin.fnx.conf.ctl.show_global_config()

@show.command()
@C.argument('worldconfig')
def world(worldconfig):
	"""prints full config to  stdout"""
	import btrwin.fnx.conf.ctl
	btrwin.fnx.conf.ctl.show_world_config(W=worldconfig)

@show.command()
def setting():
	"""prints key-value settingspair to  stdout"""
	pass
