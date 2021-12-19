#!/usr/bin/env python
import click as C
import os,shlex
import btrwin.lib as lib
import btrwin.units as unit
from colorama import Style,Fore
import subprocess
import time
G=unit.conf.get()

T= {
1:	f'Choose install name',
2:	f'Select volume to use for btrwin [0: lists detecterd disks]',
3:	f'Choose  install root [mount]/[???]/btrwin/',
4:	f'Move/Collect Wine Runners? ',
41: f'Choose folder for Wine Runners'
	}
Q ={
1:	[T[1],	C.STRING,	'btrwin'],
2:	[T[2], 	C.INT 	,	 0			],
3:	[T[3], 	C.STRING,	'opt'		],
4:	[T[4], 						'Y'			],
41: [T[41], C.STRING,	''			],

}

def ask(Q):
	return C.prompt(text=Q[0],type=Q[1],default=Q[2])
def askint(Q,VAR=None):
	return C.prompt(text=Q[0],type=Q[1],default=int(str(Q[2])))
def yes(Q):
	return C.confirm(text=Q[0],default=Q[1])
def cpy(srcdir,dest) -> None:
	"""
	copy progress
	"""
	def cprvf(src,dest):
	
			cmd=shlex.split(f'cp -rvpf {srcdir} {dest}')
			popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
			for line in iter(popen.stdout.readline, ""):
					yield line
			popen.stdout.close()
			return_code = popen.wait()
			if return_code:
					raise subprocess.CalledProcessError(return_code, cmd)
	i=0
	cur=0
	cpt = sum([len(files) for r, d, files in os.walk(srcdir)])
	with C.progressbar(label=f"Copying {os.path.split(srcdir)[1]}",length=cpt, show_eta=False) as bar:
		pct= (cpt/100)
		for path in cprvf(srcdir ,dest):
			if i == pct:
				cur=cur+1
				bar.update(cur)
			bar.update(cur)
			i=1+i
			time.sleep(0.0005)
			pass

def save_default(name, PATH):
	default= {
	'file' 		:		name,
	'section'	:		'DEFAULT',
	'NAME'		:		f'{name}',
	'PATH'		:		f'{PATH}',
	'SYS'			:		f'{PATH}/{name}',
	'LDRS'		:		f'{PATH}/{name}/loaders/',
	'WLDRS'		:		f'{PATH}/{name}/loaders/wine/',
	}
	lib.conf.set_dict(default, G)
	unit.conf.save(G)
	return unit.conf.get()
def save_init(name,mount,pth):
	init={
'file' 		:		name,
'section'	:		'PATH',
'config'	:		f'/etc/btrwin/{name}.conf',
'mount'		:		mount,
'sys'			:		'${mount}/'+ f'{pth}/btrwin',
'loaders'	:		'${SYS}/loaders',
'subv'		:		'${SYS}/subv',
}
	lib.conf.set_dict(init, G)
	unit.conf.save(G)
	return unit.conf.get()
def save_dirs(name):
	dirs={
'file' 			:		name,
'section'		:		'DIRS',
'btrwin'		:		'${SYS}',
'bin'				:		'${SYS}/bin',
'apps'			:		'${SYS}/apps',
'subv'			:		'${SYS}/subv',
'loaders'		:		'${SYS}/loaders',
'proton'		:		'${LDRS}/proton',
'wine'			:		'${LDRS}/wine',
'crossover'	:		'${LDRS}/crossover',
'default'		:		'${SYS}/default',
	}
	lib.conf.set_dict(dirs, G)
	unit.conf.save(G)
	return unit.conf.get()

def Q1():
	name=ask(Q[1])
	C.echo(f'Name: {Fore.GREEN}{name}{Style.RESET_ALL}\n')
	try:
		with open(f'/etc/btrwin/{name}.conf') as test:
			try:
				mount=G['btrwin']['PATH']['mount']
				exists=True
			except KeyError:
				exists=False
	except FileNotFoundError:
		exists=False
	if not exists:
		lib.fs.touch(f'/etc/btrwin/{name}.conf')
		unit.conf.create_new_sysconf(name)
	return name
def Q2():
	# get the currently selected disk from config if there is one
	# and adjust the default answer for the Q
	# and check number of valid answers for Q
	def askdisk():
		disk=ask(Q[2])
		return disk
	sld=unit.fs.selected_disk()
	for idx,dsk in enumerate(lib.fs.ls_disks('btrfs')):
		if sld is not None and sld in dsk[1] :
			idxsld=idx+1
			Q[2][2]=idxsld
		valid=idx+1
	disk=askdisk()
	while disk not in range(1,valid+1):
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			unit.fs.list()
			disk=askdisk()
		else:
			disk=askdisk()
	unit.fs.select_disk(disk)
	unit.fs.list()
	return unit.fs.get_list()[disk-1][1]
def Q3(mount):
	pth = ask(Q[3])
	USERHOME	=	os.environ.get('HOME')
	USER			=	os.environ.get('USER')
	PATH			=	os.path.join(mount, pth)
	unit.setup.create.sys_folders(PATH)
	unit.setup.create.sys_links(USERHOME=USERHOME,USER=USER,PATH=PATH)
	return pth
def Q4():
	return yes(Q[4])
def Q41(*a,**k):
	FPATH=f'{k["PATH"]}/{k["NAME"]}/loaders/wine'
	Q[41][2]=FPATH
	return ask(Q[41])
def Q41_copy(coldir):
	src_master=f'{os.environ.get("HOME")}/.local/share/lutris/runners/wine'
	runners=lib.fs.ls_dirs(src_master)
	for runner in runners:
		cpy(runner,coldir)
def Q41_del(coldir):
	src_master=f'{os.environ.get("HOME")}/.local/share/lutris/runners/wine'
	runners=lib.fs.ls_dirs(src_master)
	for runner in runners:
		lib.fs.rmr(runner)
		lib.fs.rmr(os.path.split(runner)[0])
@C.command()
def prompt() -> None:
	global G
	ndisk=len(unit.fs.get_list())
	def saveall():
		PATH=os.path.join(mount, pth)
		Gt=save_init(name,mount,pth)
		Gt=save_default(name,PATH)
		Gt=save_dirs(name)
		return Gt
	
	# SEQ PART1 ########
	############### Q1 #
	name=Q1()
	############### Q2 #
	mount=Q2()
	############### Q3 #
	pth=Q3(mount)
	#<> <==========> <>#
	PATH=os.path.join(mount, pth)
	G=saveall()
	#<> <==========> <>#
	# SEQ PART2 ########
	############### Q4 #
	collect_wine=Q4()
	if collect_wine:
		known_wine= unit.setup.known.wine_locs
		known_wine= unit.setup.known.wine_locs
		wine_ldrs=Q41(PATH=PATH,NAME=name)
		wloc=[known_wine[key].format(USERHOME	=	os.environ.get('HOME')) for key in known_wine]
		wldrs=[lib.fs.ls_dirs(d) for d in wloc ]
		Q41_copy(wine_ldrs)
		Q41_del(wine_ldrs)
		Q42_lns(parents

prompt()

#create dir struct on pathsys


#store most important dirs in sysconfig




#aggregate loaders/runners to btrwin and symlink original location


