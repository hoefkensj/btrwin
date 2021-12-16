#!/usr/bin/env python
import datetime
import os
from subprocess import Popen, PIPE

import debug as d
import lib.conf
import lib.fs
import units.fs.ctl
from units import conf, fs, common
import skel

#aliassing
G=conf.G()

def tpl_name(*a,**k):
		
		bit=k['bit']
		subv= G['btrwin']['PATH']['subv']
		exist= fs.btrfs.get_subvs(subv)
		prefix = 'tpl'
		win=f'Win{bit}'
		creation_date= ''.join(str(datetime.date.today()).split('-')) #get date today xxxx-xx-xx remove - and join
		version=0
		exists=True
		name=''
		while exists:
			version+=1
			init_name=f'{prefix}-{win}_{creation_date}v{version}'
			d.print(init_name)
			init_path=os.path.join(subv,init_name)
			if init_path in exist:
				d.print('found')
				exists= True
				name=init_name
			else :
				d.print('not found')
				name=init_name
				d.print(name)
				exists= False
		return name

def populate_template(tpl):
	DIRS= skel.tpl.dirs(USERNAME=os.environ['USER'])
	lib.fs.mkdirtree(DIRS['tpl'], tpl)
	d.print('dirs created')
	skel.tpl.lnks(tpl=tpl, USERNAME=os.environ['USER'])
	d.print('symlinks created')
	#link wine to /loader
	#populate /meta/bin
	#
	return True



def link_loader(tpl,loader='wine',edition='lutris',version='default' ):
	PATHSYS= G['btrwin']['PATH']['sys']
	LOADERS=os.path.join(PATHSYS,'loaders')
	LDRPATH=os.path.join(LOADERS,loader)
	PATH=f'{LDRPATH}/{edition}-{version}'
	link=os.path.join(tpl,'loader')
	d.print(PATH)
	os.symlink(PATH,link)
	return link


def boot(wineboot, env):
	process = Popen(wineboot, env=env, stdout=PIPE, universal_newlines=True, shell=True)
	ret = ''
	while True:
		output = process.stdout.readline()
		d.print(output.strip())
		# Do something else
		return_code = process.poll()
		if return_code is not None:
			ret = return_code
			# wrl(f'RETURN CODE:{return_code}')
			# Process has finished, read rest of the output
			for output in process.stdout.readlines():
				d.print(output.strip())
			break
	return ret

def new_subvol(**k):
	name 		= k['name']
	subv		= G['btrwin']['PATH']['subv']
	before		= fs.btrfs.get_subvs(subv)
	tpl			= fs.btrfs.create_subv(subv, name)
	after		= fs.btrfs.get_subvs(subv)
	diff 		= [subvol for subvol in after if subvol not in before][0]
	return name if diff == tpl else None
	
def create_template(settings):
	
	SYS= G['btrwin']
	SYS_PATH=SYS['PATH']['sys']
	SYS_SUBV=SYS['PATH']['subv']
	BIT=settings['BIT']
	
	#if name isnt specified generate one
	
	NAME		= tpl_name(bit=BIT)
	NAME	 	= new_subvol(name=NAME)
	TPL			= os.path.join(SYS_SUBV,NAME)
	POPULATED	= populate_template(tpl=TPL)
	LLDR		= link_loader(tpl=TPL,loader='wine',edition='lutris',version='default' )
	LDR_BIN		= os.path.join(LLDR, 'bin')
	
	TEMPLATE_PATH =	{
	
			'path' 	: f'{TPL}',
			'bit'	: f'{BIT}',
			'loader': f'{LLDR}'
			}
	conf.ctl.qset(file=NAME, section='PATH', key='path', value=TPL)
	conf.ctl.qset(file=NAME, section='PATH', key='loader', value=LLDR)
	# **os.environ
	#wine boot
	env = {
		'file'					:	f'{NAME}'	,
		'section'				:	'WINE_ENV',
		'WINEDEBUG' 			: 	'-all',
		'WINEARCH'				:	f'win{BIT}',
		'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
		'WINE'					: 	f'{LLDR}',
		'WINEPREFIX' 			:	f'{TPL}',
		'WINELOADER'			:	f'{LDR_BIN}/wine',
		'WINESERVER'			:	f'{LDR_BIN}/wineserver'}
	lib.conf.set_dict(env)
	
	boot(wineboot=f'{LDR_BIN}/wineboot',env=env)
	return
	
def main():

	SYS_PATH= G['btrwin']['PATH']['sys']
	setting= {
			'BIT': 64,
			'USER': os.environ.get('USER')
			}
	create_template(settings=setting)

if __name__ == '__main__':
	d.print('file1 =', G['file1'])
	main()
	


		
			