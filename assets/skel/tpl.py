#!/usr/bin/env python
import os,sys
sprint=sys.stdout.write

def dirs(USERNAME):
	DIRS= {
			'tpl': {
					'drive_c': {
							'programfiles': {},
							'programfilesx86': {},
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
					'meta'   : {
							'bin': {},
							'etc': {},
							'lib': {
									'icons': {},
									},
							'exe': {},
							},
					'apps'   : {},
					}
			}
	d.print(DIRS)
	return DIRS
	
	
def lnks(tpl):
	USER=os.environ.get('USER')
	os.chdir(os.path.join(tpl,'drive_c'))
	mklink('programfiles', 'Program Files')
	mklink('programfilesx86', 'Program Files (x86)')
	mklink('programdata', 'ProgramData')
	mklink('users', 'Users')
	os.chdir(os.path.join(tpl,'drive_c','programdata'))
	mklink('microsoft', 'Microsoft')
	os.chdir(os.path.join(tpl,'drive_c','programdata','microsoft'))
	mklink('windows', 'Windows')
	os.chdir(os.path.join(tpl,'drive_c','programdata','microsoft','windows'))
	mklink('../../start', 'Start Menu')
	os.chdir(os.path.join(tpl,'drive_c','users'))
	mklink(USER, 'steamuser')
	os.chdir(os.path.join(tpl,'drive_c','users',USER))
	USERHOME=os.path.join('/home',USER)
	mklink(os.path.join(USERHOME, 'Documents'), 'Documents')
	mklink(os.path.join(USERHOME, 'Downloads'), 'Downloads')
	mklink(os.path.join(USERHOME, 'Music'), 'Music')
	mklink(os.path.join(USERHOME, 'Pictures'), 'Pictures')
	mklink(os.path.join(USERHOME, 'Videos'), 'Videos')
	return

def mklink(src,lnk):
		os.remove(lnk) if os.path.exists(lnk) else None
		sprint(f'creating symlink [{src}--> {lnk} ...')
		mklink(src,lnk)
		sprint('Done\n')
		
