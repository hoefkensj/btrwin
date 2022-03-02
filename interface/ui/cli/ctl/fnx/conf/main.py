#!/usr/bin/env python
import click as C




@C.group()
def conf():
	"""conf help"""
	pass

@conf.command()
def paths():
	import btrwin.fnx.conf.ctl
	btrwin.fnx.conf.ctl.show_config_paths()


import btrwin.interface.ui.cli.ctl.fnx.conf.ctl
conf.add_command(btrwin.interface.ui.cli.ctl.fnx.conf.ctl.ctl)


import btrwin.interface.ui.cli.ctl.fnx.conf.show.show
conf.add_command(btrwin.interface.ui.cli.ctl.fnx.conf.show.show.show)

import btrwin.interface.ui.cli.ctl.fnx.conf.create.create
conf.add_command(btrwin.interface.ui.cli.ctl.fnx.conf.create.create.create)


import btrwin.interface.ui.cli.ctl.fnx.conf.load.load
conf.add_command(btrwin.interface.ui.cli.ctl.fnx.conf.load.load.load)

