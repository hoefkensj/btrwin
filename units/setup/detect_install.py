#!/usr/bin/env python
import os

import lib as lib
import units as units
from configure.Q import hardcoded
from configure.cli import G


def check_inst(name):
		exist_cfg= True if os.path.exists('/etc/btrwin/{name}.conf') else False
		exist_keyval= True if dict(G['btrwin']['PATH']).get('mount') else False
		return exist_cfg and exist_keyval
		
		dir_sysconf= hardcoded['PATH']['dir_sysconf']
		if not os.path.exists(dir_sysconf):
			
			#TODO:			#sudo create the sysconfdir Z&& sudo chmod 664 && CHOWN root:btrwin

		
		# if not exists:
		# 	lib.fs.touch(f'/etc/btrwin/{name}.conf')
		# 	units.conf.ctl.create_new_sysconf(name)
		# if not os.path.exists(os.path.join(dir_sysconf , f'{name}.conf')):
		# 				lib.fs.touch(os.path.join(dir_sysconf , f'{name}.conf'))
		# 				units.conf.ctl.create_new_sysconf(name)