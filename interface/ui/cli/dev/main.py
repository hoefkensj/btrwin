#!/usr/bin/env python
import click as C

from . import test
@C.group()
def entry_point():
	pass
    
# entry_point.add_command(fnx.check.check)
entry_point.add_command(test.test)







entry_point(prog_name="btrwin: DEVELOPER MODE")


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
