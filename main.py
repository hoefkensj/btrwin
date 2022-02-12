import types

ui= types.SimpleNamespace()
def interface_ui_cli_ctl(ui):
	import btrwin.interface.ui.cli.ctl
	ui.cli_ctl = btrwin.interface.ui.cli.ctl.main.entry_point
	return ui

def interface_ui_default(ui):
	ui.default=interface_ui_cli_ctl(ui)
	return ui
	
ui=interface_ui_default(ui)
