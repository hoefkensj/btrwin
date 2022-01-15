#!/usr/bin/env python
import click as C
import btrwin.units as units




@C.group()
def show():
	"""btrtfs help"""

	pass
	#################

@show.command()
def all():
	"""prints full config to  stdout"""
	units.conf.show()
	pass

@show.command()
def setting():
	"""prints key-value settingspair to  stdout"""
	pass
