#!/usr/bin/env python
import click as C

from btrwin.units.ui.cli import conf
from btrwin.units.ui.cli import fs
from btrwin.units.ui.cli import setup

@C.group()
def entry_point():
    pass

entry_point.add_command(fs.fs)
entry_point.add_command(conf.conf)
entry_point.add_command(setup.setup)



# from btrwin.cli import fs as cli_fs
# from .group2 import commands as group2
#
# @C.group()
# def entry_point():
#     pass
#
# entry_point.add_command(group1.command_group)
# entry_point.add_command(group2.version)
#
# @C.group()
# def cli():
# 	"""btrwin  help"""
# 	fs()
#
# #################
#
# #################
#
#
#
# #################
# @cli.group()
# def prefix():
# 	"""prefix help"""
# 	pass
# 	@prefix.group()
# 	def loader():
# 		"""prefix help"""
# 		pass
# 	@prefix.group()
# 	def meta():
# 		"""prefix help"""
# 		pass
# 		#################
# 		@meta.group()
# 		def bin():
# 			"""bin help"""
# 			pass
# 		@meta.group()
# 		def exec():
# 			"""exec help"""
# 			pass
# 	#################
# #################
#
# @prefix.group()
# def template():
# 	"""prefix help"""
# 	pass
#
# ####################################################################################
#
#
#
#
