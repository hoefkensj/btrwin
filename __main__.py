#!/usr/bin/env python
import os
import btrwin
def PYTHONPATH_ADD_REQUIRED_FOLDERS():
	PYPATHS=os.environ['PYTHONPATH'].split(':') if os.environ.get('PYTHONPATH') else []
	PKGDIR=os.path.dirname(__file__)
	PARDIR=os.path.dirname(PKGDIR)
	os.environ['PYTHONPATH']	= '{}:{}'.format(PKGDIR, ':'.join(PYPATHS)) if PKGDIR not in PYPATHS else PYPATHS
	os.environ['PYTHONPATH']	= '{}:{}'.format(PARDIR, ':'.join(PYPATHS)) if PARDIR not in PYPATHS else PYPATHS

def procedure_user():

	btrwin.main.env_store()
	
def procedure_root():
	import btrwin.main
	print(f'running as  UID: {os.geteuid()} ({os.environ.get("USER")}) [OK]')
	btrwin.main.env_load()


def run_developer_cli():
	exec=btrwin.main.ui(prog_name="btrwin: DEVELOPER MODE")

def run_default():
	exec=btrwin.main.interface_ui_cli_ctl(prog_name="btrwin")
	
if os.geteuid() == 0:	procedure_root()
else: procedure_user()

run_default()
