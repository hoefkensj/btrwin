#!/usr/bin/env python
import os
import time
import click as C

import btrwin.lib as lib
import btrwin.units as units
import btrwin.configure.Q as Q

import assets.locale.enUS_configure_cli as LC


cp=lib.fs.cp

G=units.conf.load()

LC_QT= LC.QTEXT
Q ={
1.01_01:	[LC_QT[1.01_01],	C.STRING,	'btrwin'],
1.02_01:	[LC_QT[1.02_01], 	C.INT 	,	 0			],
1.03_01:	[LC_QT[1.03_01], 	C.STRING,	'opt'		],
1.04_00:	[LC_QT[1.04_00], 						'Y'			],
1.04_01: 	[LC_QT[1.04_01], 	C.STRING,	''			],

}

def ask(Q):
	return C.prompt(text=Q[0],type=Q[1],default=Q[2])
def askint(Q):
	return C.prompt(text=Q[0],type=Q[1],default=int(str(Q[2])))
def ok(Q):
	return C.confirm(text=Q[0],default=Q[1])



def cpy(srcdir,dest) -> None:
	"""
	copy progress
	"""
	i=0
	cur=0
	cpt = sum([len(files) for r, d, files in os.walk(srcdir)])
	with C.progressbar(label=f"Copying {os.path.split(srcdir)[1]}",length=cpt, show_eta=False) as bar:
		pct= (cpt/100)
		for path in cp(srcdir, srcdir, dest):
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
	units.conf.save(G)
	return units.conf.load()
def save_tluafed(name, PATH):
	tluafed= {
		'file' 		:		name,
		'section'	:		'TLUAFED',
		'NAME'		:		f'{name}',
		'PATH'		:		f'{PATH}',
		'SYS'			:		f'{PATH}/{name}',
		'LDRS'		:		f'{PATH}/{name}/loaders/',
		'WLDRS'		:		f'{PATH}/{name}/loaders/wine/',
		}
	lib.conf.set_dict(tluafed, G)
	units.conf.save(G)
	return units.conf.load()
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
	units.conf.save(G)
	return units.conf.load()
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
	units.conf.save(G)
	return units.conf.load()
def saveall(n,m,p):
	PATH=os.path.join(m, p)
	Gt=save_init(n,m,p)
	Gt=save_default(n,PATH)
	GT=save_tluafed(n,PATH)
	Gt=save_dirs(n)
	return Gt


@C.command()
def prompt() -> None:
	global G
	ndisk=len(units.fs.get_list())
	
	# SEQ PART1 ########
	name=Q.Q1()
	mount=Q.Q2()
	pth=Q.Q3(mount)
	G=saveall(name,mount, pth)

	# SEQ PART2 ########

	if Q.Q4_0():
		known_wine= units.setup.known.wine_locs
		wloc=[known_wine[key].format(USERHOME	=	os.environ.get('HOME')) for key in known_wine]
		wldrs=[lib.fs.ls_dirs(d) for d in wloc if os.path.exists(d) ]
		wine_ldrs=Q.Q4_1(PATH=PATH,NAME=name)
		if wldrs:
			Q4_1_copy(wine_ldrs)
			Q4_1_del(wine_ldrs)
		#Q41_lns('{parents}')

prompt()

#create dir struct on pathsys


#store most important dirs in sysconfig




#aggregate loaders/runners to btrwin and symlink original location


