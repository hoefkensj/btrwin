#!/usr/bin/env python

def ctl():
	import btrwin.interface.ui.cli.ctl.main
	btrwin.interface.ui.cli.ctl.main.entry_point_ctl(prog_name="BTRWIN:::CTL-MODE")
def dev():
	import btrwin.interface.ui.cli.dev.main
	btrwin.interface.ui.cli.dev.main.entry_point_dev(prog_name="BTRWIN:::DEV-MODE")