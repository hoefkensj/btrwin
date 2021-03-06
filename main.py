import os
import pickle


def interface_ui_cli_ctl(**k):
	import btrwin.interface.ui.cli.main
	return btrwin.interface.ui.cli.main.ctl()


def interface_ui_cli_dev(**k):
	import btrwin.interface.ui.cli.main
	return btrwin.interface.ui.cli.main.dev()
	
def interface_ui_cli_setup(**k):
	import btrwin.interface.ui.cli.main
	return btrwin.interface.ui.cli.main.setup()



	# iface = os.environ.get('BTRWIN_iface')
	# print(os.environ.get('BTRWIN_iface') or 'default' )
	#
	# mode	=	os.environ.get('BTRWIN_mode')
	# print(os.environ.get('BTRWIN_mode') or 'default' )
	# cli = interface_ui_cli()
	# interfaces_cfg= {'default' 	: interface_ui_cli(),
	# 									'cli'			:	{
	# 																										'default'		: 	interface_ui_cli_ctl(**k),
	# 																										'ctl'				: 	interface_ui_cli_ctl(**k),
	# 																										'dev' 			: 	interface_ui_cli_dev(**k),
	# 																										},
	#
	#
	# 									'term'		:	{None,},
	# 									'api'			:	{None,},
	# 									}
	# run=interfaces_cfg[iface][mode]
	# print(repr(run))
	# return run

def super_su(**k):
	import sys
	print(f'GOT UID: {os.geteuid()}({os.environ.get("USER")}) NEED UID: 0 (root)!')
	args = [f'sudo env PYTHONPATH="{os.environ.get("PYTHONPATH")}" ', sys.executable] + sys.argv # + [os.environ]
	os.execvpe('sudo', args, os.environ)


def reload_env(**k):
	import sys
	args = [f'env PYTHONPATH="{os.environ.get("PYTHONPATH")}" ', sys.executable] + sys.argv # + [os.environ]
	PARENTFOLDER=os.path.split(os.path.split(sys.argv[0])[0])
	if not os.environ.get("PYREL"):
		os.environ["PYTHONPATH"]=f'{PARENTFOLDER[0]}:{os.environ.get("PYTHONPATH")}'
		os.environ['PYREL'] = '1'
		os.execvpe('/usr/bin/env', args, os.environ)

	
		



def env_load():
	with open('/tmp/REROOT_USER.env','rb') as f :
		env_tmp=pickle.load(f)
	#only add keys that are missing, avoids overwriting USER ,USERHOME , ...
	os.environb=env_tmp #{key : env_tmp[key] for key in env_tmp.keys()if key not in os.environ.keys() }
	

def env_store():
	with open('/tmp/REROOT_USER.env' , 'wb') as f:
		pickle.dump({**os.environ},f)
		
		
reload_env()