#!/usr/bin/env python
import os
import debug as d
def dirs():
	DIRS= {
			'sys': {
					'btrwin': {
							'bin'    : {},
							'apps'   : {},
							'subv'   : {},
							'ldrs'   : {
									'proton'   : {},
									'wine'     : {},
									'crossover': {}
									},
							'default': {},
							},
					}
			}
	return DIRS
	
	
def lnks(path):
	os.chdir(os.path.join(path,'btrwin','subv'))
	d.print(f"in {os.path.join(path,'btrwin','subv')} :")
	os.symlink('tpl_placeholder','tpl_default')
	d.print(f"created symlink: tpl_placeholder ->'tpl_default'")
	os.symlink('default', 'home-wine')
	os.chdir(os.path.join(path,'btrwin','default'))
	os.symlink('../subv/default', 'prefix')
	os.symlink('../ldrs/wine/default', 'wine')
	os.symlink('../ldrs/proton/default', 'proton')
	os.symlink('~/.wineuser', 'user')
	os.chdir('~/')
	os.symlink(os.path.join(path,'default','prefix') ,'.wine')
	os.symlink(os.path.join(path,'default','user') ,'.btrwinuser')
	os.chdir('/opt')
	os.symlink(os.path.join(path,'btrwin'),'btrwin')
	return