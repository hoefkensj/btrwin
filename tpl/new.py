#!/usr/bin/env python
import confctl
import fsctl
from functools import partial
import debug as d
import os,datetime
import skel
from subprocess import Popen,PIPE

def tpl_name(*a,**k):
		
		bit=k['bit']
		subv=confctl.glob['betterwin']['PATH']['subv']
		exist= fsctl.btrfsctl.get_subvs(subv)
		prefix = 'tpl'
		
		win=f'Win{bit}'
		creation_date= ''.join(str(datetime.date.today()).split('-')) #get date today xxxx-xx-xx remove - and join
		version=0
		exists=True
		while exists:
			version+=1
			init_name=f'{prefix}-{win}_{creation_date}v{version}'
			d.print(init_name)
			init_path=os.path.join(subv,init_name)
			if init_path in exist:
				d.print('found')
				exists= True
			else :
				d.print('not found')
				name=init_name
				d.print(name)
				exists= False
		return name

def populate_template(tpl):
	DIRS=skel.tpl.dirs(USERNAME=os.environ['USER'])
	create_struct(DIRS['tpl'], tpl)
	d.print('dirs created')
	skel.tpl.lnks(tpl=tpl,USERNAME=os.environ['USER'])
	d.print('symlinks created')
	#link wine to /loader
	#populate /meta/bin
	#
	return True

def create_struct(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			os.makedirs(next_path)
			create_struct(info, next_path)
	return

def link_loader(tpl,loader='wine',edition='lutris',version='default' ):
	PATHSYS=confctl.glob['betterwin']['PATH']['sys']
	LOADERS=os.path.join(PATHSYS,'loaders')
	LDRPATH=os.path.join(LOADERS,loader)
	PATH=f'{LDRPATH}/{edition}-{version}'
	link=os.path.join(tpl,'loader')
	d.print(PATH)
	os.symlink(PATH,link)
	return link

def boot(wineboot,env):
	sproc= partial(Popen, env=env, stdout=PIPE,universal_newlines=True,shell=True)
	
	process=Popen(wineboot ,env=env, stdout=PIPE,universal_newlines=True,shell=True)
	ret = ''
	while True:
		output = process.stdout.readline()
		d.print(output.strip())
		# Do something else
		return_code = process.poll()
		if return_code is not None:
			ret= return_code
			#wrl(f'RETURN CODE:{return_code}')
			# Process has finished, read rest of the output
			for output in process.stdout.readlines():
				d.print(output.strip())
			break
	return ret

def new_subvol(**k):
	name 		= k['name']
	subv		= confctl.glob['betterwin']['PATH']['subv']
	before		= fsctl.btrfsctl.get_subvs(subv)
	tpl			= fsctl.btrfsctl.create_subv(subv, name)
	after		= fsctl.btrfsctl.get_subvs(subv)
	diff 		= [subvol for subvol in after if subvol not in before][0]
	return name if diff == tpl else None
	
def create_template(settings):
	
	SYS=confctl.glob['betterwin']
	SYS_PATH=SYS['PATH']['sys']
	SYS_SUBV=SYS['PATH']['subv']
	BIT=settings['BIT']
	
	#if name isnt specified generate one
	
	NAME		= tpl_name(bit=BIT)
	NAME	 	= new_subvol(name=NAME)
	TPL			= os.path.join(SYS_SUBV,NAME)
	POPULATED	= populate_template(tpl=TPL)
	LLDR		= link_loader(tpl=TPL,loader='wine',edition='lutris',version='default' )
	LDR_BIN		= os.path.join(LLDR,'bin')
	
	TEMPLATE_PATH =	{
	
			'path' 	: f'{TPL}',
			'bit'	: f'{BIT}',
			'loader': f'{LLDR}'
			}
	confctl.set(file=NAME, section='PATH', key='path', value=TPL)
	confctl.set(file=NAME, section='PATH', key='loader', value=LLDR)
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
	confctl.confctl.set_dict(env)
	
	boot(wineboot=f'{LDR_BIN}/wineboot',env=env)
	return
	
def main():

	SYS_PATH=confctl.glob['betterwin']['PATH']['sys']
	set={}
	set['BIT']=64
	set['USER']=os.environ.get('USER')
	create_template(settings=set)

if __name__ == '__main__':
	d.print('file1 =', confctl.glob['file1'])
	main()
	


		
			