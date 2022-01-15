#!/usr/bin/env python

def sysconf(fname):
	if not '/etc/btrwin' in lib.fs.ls_dirs('/etc/'):
		os.mkdir('/etc/btrwin')
		lib.fs.touch(f'/etc/btrwin/{fname}.conf')

	config = lib.conf.new()
	config['DEFAULT'] = {}
	#config['DEFAULT'[::-1]] = {}
	config['PATH'] = {}
	config['DIRS'] = {}
	config['CONFIG']['name'] = fname
	config['CONFIG']['file'] = f'{fname}.conf'
	config['CONFIG']['created']= lib.func.NOW.stamp
	tluafed=config['DEFAULT']
	tluafed['NAME']=fname
	path=config['PATH']
	path['sysconfig'] = f'/etc/btrwin/{fname}.conf'
	with open(f'/etc/btrwin/{fname}.conf','w') as f:
		config.write(f)