#!/usr/bin/env python
import os

import lib.fs


DIRS= {
			'sys': {
					'btrwin': {
							'bin'    : {},
							'apps'   : {},
							'subv'   : {},
							'loaders'   : {
									'proton'   : {},
									'wine'     : {},
									'crossover': {}
									},
							'default': {},
							},
					}
			}

	
def links(path):
	links={
	os.path.join(path,'btrwin','subv') 			: [		('tpl_placeholder','tpl_default'),('default', 'home-wine')],
	os.path.join(path,'btrwin','default')		:	[		('../subv/default', 'prefix'),('../loaders/wine/default', 'wine'),('../loaders/proton/default', 'proton'),('~/.wineuser', 'user')],
	os.environ.get('HOME') 									:	[		(os.path.join(path,'default','prefix') ,'.wine'),(os.path.join(path,'default','user') ,'.btrwinuser')],
	'/opt'																	:	[		(os.path.join(path,'btrwin'),'btrwin'),]
		}
	return links