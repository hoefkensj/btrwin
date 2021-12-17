#!/usr/bin/env python

SYS={
'DIRS'	: {
'sys': {
'btrwin'		: {		'bin'    		: {},
															'apps'   		: {},
															'subv'   		: {},
															'loaders'   : {		'proton'   : {},
																								'wine'     : {},
																								'crossover': {},		},
															'default'		: {},		},
},}	,
'LINKS'	: {
'{PATH}/btrwin/subv' 		: {	'tpl_placeholder'								:	'tpl_default'	,
													 	'default'												:	'home-wine'		,	}	,
'{PATH}/btrwin/default' :	{	'../subv/default'								:	'prefix'			,
													 	'../loaders/wine/default'				:	'wine'				,
													 	'./loaders/proton/default'			:	'proton'			,
													 	'~/.wineuser'										:	'user'				,	}	,
'{USERHOME}'						:	{	'{PATH}/default/prefix'					:	'.wine'				,
													 	'{PATH}/default/user'						:	'.btrwinuser'	,	}	,
'/opt'									:	{	'{PATH}/btrwin'									:	'btrwin'			,
																																								}	,
}	,
}


















# def links(path):
# 	links={
# 	os.path.join(path,'btrwin','subv') 			: [		('tpl_placeholder','tpl_default'),('default', 'home-wine')],
# 	os.path.join(path,'btrwin','default')		:	[		('../subv/default', 'prefix'),('../loaders/wine/default', 'wine'),('../loaders/proton/default', 'proton'),('~/.wineuser', 'user')],
# 	os.environ.get('HOME') 									:	[		(os.path.join(path,'default','prefix') ,'.wine'),(os.path.join(path,'default','user') ,'.btrwinuser')],
# 	'/opt'																	:	[		(os.path.join(path,'btrwin'),'btrwin'),]
# 		}
# 	return links
#
# LINKS= {
# 				'{PATH}/btrwin/subv' 		: [{'src' : 'tpl_placeholder'						,		'lnk' : 'tpl_default'}	,
# 																	{	'src'	:	'default'										,		'lnk'	:	'home-wine'}		,	]	,
#
# 				'{PATH}/btrwin/default' :	[{'src' : '../subv/default'						,		'lnk' : 'prefix'}				,
# 																	{	'src'	:	'../loaders/wine/default'		,		'lnk'	:	'wine'}					,
# 																	{	'src'	:	'./loaders/proton/default'	,		'lnk'	:	'proton'}				,
# 																	{	'src'	:	'~/.wineuser'								,		'lnk'	:	'user'}					,	]	,
#
# 				'{USERHOME}'						:	[{'src' : '{PATH}/default/prefix'			,		'lnk'	:	'.wine'}				,
# 																	{	'src' : '{PATH}/default/user'				,		'lnk'	:	'.btrwinuser'}	,	]	,
#
# 				'/opt'									:	[{'src'	:	'{PATH}/btrwin'							,		'lnk'	:	'btrwin'}				,	]	,
# 	}