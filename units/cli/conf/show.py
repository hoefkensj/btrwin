#!/usr/bin/env python
import click as C
from btrwin.units.conf.ctl import show_global_config



@C.group()
def show():
	"""btrtfs help"""
	pass
	#################

@show.command()
def all():
	"""prints full config to  stdout"""
	show_global_config()
	pass

@show.command()
def setting():
	"""prints key-value settingspair to  stdout"""
	pass
