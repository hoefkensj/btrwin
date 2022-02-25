#!/usr/bin/env python
import click as C


@C.group()
def test():
	"""test help"""
	pass


@C.group('ansi')
def ansi()
	"""
	test ansi functions
	:return:  None
	"""
	C.help_option()
	
@ansi.command('markup')
@C.option('-r','--range', 'range' ,  help='INT[0-256]|RANGE (0-255) | FULL | ALL' )
def markup(range):
	"""test ansi markup rangesc"""
	import btrwin.lib.ANSI_markup
	btrwin.lib.ANSI_markup.markup_test(range)

test.add_command(ansi)