#!/usr/bin/env python
import conf
import btrfs
from functools import partial
import debug as d
import os,datetime,sys
import skel
from subprocess import Popen,PIPE





def create_template(*,USERNAME,settings,name):


		
	def new_subvol():
	
		def tpl_name(*,exist,bit,name,subv):  #creates the name for a template tpl-Win64_YYYYMMDDvX
			prefix = name
			win=f'Win{bit}'
			creation_date= ''.join(str(datetime.date.today()).split('-')) #get date today xxxx-xx-xx remove - and join
			version=0
			exists=True
			while exists:
				version+=1
				init_name=f'{prefix}-{win}_{creation_date}v{version}'
				d.print(init_name)
				init_path=os.path.join(subv,init_name)
				if init_path in existing:
					d.print('found')
					exists= True
				else :
					d.print('not found')
					name=init_name
					d.print(name)
					exists= False
			return name
	
	
		existing	= btrfs.get_subvs(dir_subv)
		name 		= tpl_name(exist=existing,bit=settings['bit'],subv=dir_subv)
		before		= btrfs.get_subvs(dir_subv)
		btrfs.create_subv(dir_subv, name)
		dir_tpl		= os.path.join(dir_subv,name)
		after		= btrfs.get_subvs(dir_subv)
		diff 		= [subv for subv in after if subv not in before][0]
		if diff == dir_tpl :
			d.print('successfully created subvolume', name)
			return name
		#TODO write settings to meta/etc/
		#Todo write settings to ~/.config/?/tplname
		return False
		
	def populate_template(tpl):
		DIRS=skel.tpl.dirs(USERNAME=USERNAME)
		create_struct(DIRS['tpl'], tpl)
		d.print('dirs created')
		skel.tpl.lnks(tpl=tpl,USERNAME=USERNAME)
		d.print('symlinks created')
		#link wine to /loader
		#populate /meta/bin
		#
		return True
	
	def link_loader(tpl,loader='wine',edition='lutris',version='default' ):
		PATHSYS=conf.glob['SYS']['PATH']['sys']
		LOADERS=os.path.join(PATHSYS,'loaders')
		LDRPATH=os.path.join(LOADERS,loader)
		PATH=f'{LDRPATH}/{edition}-{version}'
		link=os.path.join(tpl,'loader')
		d.print(PATH)
		os.symlink(PATH,link)
		return link
	
	def boot(wineboot,env):
		sproc= partial( Popen, env=env, stdout=PIPE,
					universal_newlines=True,
					shell=True)
		process=sproc(wineboot)
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
	
	PATHSYS		= conf.glob['SYS']['PATH']['sys']   #gets the system (betterwin) directory form config
	dir_subv	= os.path.join(PATHSYS,'subv')		#appends subv to the above for the location of the subvolumes
	#if name isnt specified generate one
	existing	= btrfs.get_subvs(dir_subv)
	
	
		#appends the name for the subvolume
	created 	= new_subvol()
	dir_tpl		= os.path.join(dir_subv,created)
	status 		= populate_template(tpl=dir_tpl) if created else False
	lldr		= link_loader(tpl=dir_tpl)
	wineboot	= os.path.join(lldr,'bin','wineboot')
	
	#wine boot
	env = {
		**os.environ,
		'WINEDEBUG' 			: 	'-all',
		'WINEARCH'				:	'win64',
		'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
		'WINEPREFIX' 			:	f'{dir_tpl}',
		'WINELOADER'			:	f'{lldr}/bin/wine',
		'WINESERVER'			:	f'{lldr}/bin/wineserver'
	}
	boot(wineboot=wineboot,env=env)
	
	
	
	
	return status
	
	# create_template=partial(f_create_template ,glob_config=

	
def create_struct(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			os.makedirs(next_path)
			create_struct(info, next_path)
	return
	
def main():

	PATHSYS=conf.glob['SYS']['PATH']['sys']
	d.print(PATHSYS)
	set={}
	set['bit']=64
	USER=os.environ.get('USER')
	dir_subv=os.path.join(PATHSYS,'subv')
	list=btrfs.get_subvs(dir_subv)
	d.print(list)
	create_template(settings=set,USERNAME=USER)





if __name__ == '__main__':
	# print(conf.glob)
	# print('SYS =')
	# print("conf.glob['SYS']['GENERAL']\t\t\t\t	= " 	,conf.glob['SYS']['GENERAL'])
	# print("conf.glob['SYS']['GENERAL']['name']\t\t	= " ,conf.glob['SYS']['GENERAL']['name'])
	# print("conf.glob['SYS']['GENERAL']['btrmnt']\t	= " ,conf.glob['SYS']['GENERAL']['btrmnt'])
	# print("conf.glob['SYS']['PATH']\t\t\t\t	= " 		,conf.glob['SYS']['PATH'])
	# print("conf.glob['SYS']['PATH']['sys']\t\t\t	= " ,conf.glob['SYS']['GENERAL']['name'])


	d.print('file1 =',conf.glob['file1'])
	main()
	


		
			