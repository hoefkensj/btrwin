#!/usr/bin/env python
import os

def PYTHONPATH_ADD_REQUIRED_FOLDERS():
	PYPATHS=os.environ['PYTHONPATH'].split(':') if os.environ.get('PYTHONPATH') else []
	PKGDIR=os.path.dirname(__file__)
	PARDIR=os.path.dirname(PKGDIR)
	os.environ['PYTHONPATH']	= '{}:{}'.format(PKGDIR, ':'.join(PYPATHS)) if PKGDIR not in PYPATHS else PYPATHS
	os.environ['PYTHONPATH']	= '{}:{}'.format(PARDIR, ':'.join(PYPATHS)) if PARDIR not in PYPATHS else PYPATHS

def procedure_user():
	import btrwin.main
	btrwin.main.env_store()
	
def procedure_root():
	import btrwin.main
	print(f'running as  UID: {os.geteuid()} ({os.environ.get("USER")}) [OK]')
	btrwin.main.env_load()


def run_developer_cli():
	import btrwin.main
	exec=btrwin.main.ui(prog_name="btrwin: DEVELOPER MODE")

def select_interface(**k):
	import btrwin.main
	modes={
	'default' : btrwin.main.interface_ui_cli_ctl,
	'ctl' : btrwin.main.interface_ui_cli_ctl,
	'dev' : btrwin.main.interface_ui_cli_dev,
		}
	return modes.get(k.get('mode') or 'default')

if os.geteuid() == 0:	procedure_root()
else: procedure_user()

run=select_interface(mode=(os.environ.get('BTRWIN_MODE') or 'default'))
run()