#!/usr/bin/env python
import click as C

@C.group()
def entry_point_ctl():
	"""	help entrypoint : Controll"""
	pass
	
import btrwin.interface.ui.cli.ctl.fnx.conf.main
import btrwin.interface.ui.cli.ctl.fnx.ctl.main
import btrwin.interface.ui.cli.ctl.fnx.fs.main
# entry_point.add_command(fnx.check.check)
entry_point_ctl.add_command(btrwin.interface.ui.cli.ctl.fnx.conf.main.conf)
entry_point_ctl.add_command(btrwin.interface.ui.cli.ctl.fnx.ctl.main.ctl)
# entry_point.add_command(fnx.file.file)
entry_point_ctl.add_command(btrwin.interface.ui.cli.ctl.fnx.fs.main.fs)
# entry_point.add_command(fnx.loader.loader)
# entry_point.add_command(fnx.prefix.prefix))


# 	fs()
# from btrwin.ctl import fs as cli_fs
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
# def ctl():
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
# @ctl.group()
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
