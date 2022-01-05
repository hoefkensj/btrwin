#!/usr/bin/env python
import click as C

@C.command()
def conf():
	"""conf help"""
	pass
	@conf.group()
	def ctl():
		"""conf help"""
		pass
	@conf.group()
	def pfx():
		"""conf help"""
		pass
	@conf.group()
	def init():
		"""conf help"""
		pass
#################