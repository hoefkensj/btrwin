#!/usr/bin/env python
import debug as d
import os
def dirs(USERNAME):
	DIRS={}
	DIRS['tpl'] ={
			'drive_c':{
				'programfiles': {},
				'programfilesx86':{},
				'programdata': {
						'microsoft': {
							'windows': {},
						},
				},
				'users': {
					USERNAME: {
						'appdata': {
							'roaming': {},
						},
					},
				},
				'start': {},
			},
			'meta':{
				'bin': {},
				'etc':	{},
				'lib': {
					'icons' : {},
						},
				'exe': {},
			},
			'apps' : {},
	}
	d.print(DIRS)
	return DIRS
	
	
def lnks(tpl,USERNAME):
	os.chdir(os.path.join(tpl,'drive_c'))
	os.symlink('programfiles', 'Program Files')
	os.symlink('programfilesx86', 'Program Files (x86)')
	os.symlink('programdata', 'ProgramData')
	os.symlink('users', 'Users')
	os.chdir(os.path.join(tpl,'drive_c','programdata'))
	os.symlink('microsoft', 'Microsoft')
	os.chdir(os.path.join(tpl,'drive_c','programdata','microsoft'))
	os.symlink('windows', 'Windows')
	os.chdir(os.path.join(tpl,'drive_c','programdata','microsoft','windows'))
	os.symlink('../../start', 'Start Menu')
	os.chdir(os.path.join(tpl,'drive_c','users'))
	os.symlink(USERNAME, 'steamuser')
	os.chdir(os.path.join(tpl,'drive_c','users',USERNAME))
	USERHOME=os.path.join('/home',USERNAME)
	os.symlink(os.path.join(USERHOME, 'Documents'), 'Documents')
	os.symlink(os.path.join(USERHOME, 'Downloads'), 'Downloads')
	os.symlink(os.path.join(USERHOME, 'Music'), 'Music')
	os.symlink(os.path.join(USERHOME, 'Pictures'), 'Pictures')
	os.symlink(os.path.join(USERHOME, 'Videos'), 'Videos')
	return