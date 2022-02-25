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

def run_default_cli():
	# PYTHONPATH_ADD_REQUIRED_FOLDERS()
	import btrwin.main
	btrwin.main.ui.default(prog_name="btrwin")

if os.geteuid() == 0:	procedure_root()
else: procedure_user()
run_default_cli()