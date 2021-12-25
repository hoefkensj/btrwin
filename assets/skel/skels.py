#!/usr/bin/env python

SKELLS= {
'SYS'	:	{
	'DIRS'		: {
									'sys'		: {
									'btrwin'	: {
										'bin' 		: {},
											'apps'   		: {},
											'subv'   		: {},
											'loaders'   : {
												'proton'   : {},
												'wine'     : {},
												'crossover': {},},
											'default'		: {},	},},},
	'LINKS'		: {
									'{PATH}/btrwin/subv' 															: 		{
																																						'tpl_placeholder'									:			'tpl_default'							,
																																						'default'													:			'home-wine'								,},
									'{PATH}/btrwin/default' 													:			{
																																						'../subv/default'									:			'prefix'									,
																																						'../loaders/wine/default'					:			'wine'										,
																																						'./loaders/proton/default'				:			'proton'									,
																																						'~/.wineuser'											:			'user'										,},
									'{USERHOME}'																			:			{
																																						'{PATH}/btrwin/default/prefix'		:			'.wine'										,
																																						'{PATH}/btrwin/default/user'			:			'.btrwinuser'							,},
									'/opt'																						:			{
																																						'{PATH}/btrwin'										:			'btrwin'									,},},},
'TPL'		:	{
	'DIRS'		:	{
									'tpl' 																						:			{
									'drive_c' 																				:			{
										'programfiles' 																	:			{},
										'programfilesx86' 															:			{},
										'programdata' 																	:			{
											'microsoft' 																	:			{
												'windows' 																	:			{},},},
										'users' 																				:			{
											'{USERNAME}' 																	:			{
												'appdata' 																	:			{
													'roaming' 																:			{},},},},
										'start' 																				:			{},},
									'meta'    																				:			{
										'bin' 																					:			{},
										'etc' 																					:			{},
										'lib' 																					:			{
											'icons' 																			:			{},},
										'exe' 																					:			{},},
									'apps'  																					:			{},},},
	'LINKS'		:	{
									'{PATH}/drive_c'																	:			{
																																						'programfiles'										:			'Program Files'						,
																																						'programfilesx86'									:			'Program Files (x86)'			,
																																						'programdata'											:			'ProgramData'							,
																																						'users'														:			'Users'										,},
									'{PATH}/drive_c/programdata'											:			{
																																						'microsoft'												:			'Microsoft'								,},
									'{PATH}/drive_c/programdata/microsoft'						:			{
																																						'windows'													:			'Windows'									,},
									'{PATH}/drive_c/programdata/microsoft/windows'		:			{
																																						'../../start'											:			'Start Menu'							,},
									'{PATH}/drive_c/users'														:			{
																																						'{USER}'													: 		'steamuser'								,},
									'{PATH}/drive_c/users/{USER}'											: 		{
																																						'{USERHOME}/Documents'						:			'Documents'								,
																																						'{USERHOME}/Downloads'						:			'Downloads'          			,
																																						'{USERHOME}/Music'								:			'Music'              		 	,
																																						'{USERHOME}/Pictures'							:			'Pictures'           		 	,
																																						'{USERHOME}/Videos'								:			'Videos'             		 	,},},},}
    							
                	
                	
