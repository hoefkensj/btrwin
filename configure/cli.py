#!/usr/bin/env python
import click as C
import os
import btrwin.lib as lib
import btrwin.units as unit

G=unit.conf.get()


P=dict()


T= {
1:	f'Choose install name',
2:	f'Select volume to use for btrwin [0: lists detecterd disks]',
3:	f'Choose  install root [mount]/[???]/btrwin/',
	}

Q ={
1:	[T[1],	C.STRING,	'btrwin'],
2:	[T[2], 	C.INT 	,	 0			],
3:	[T[3], 	C.STRING,	'opt'		],
}

def pct(qnr):
	pct=int(((qnr/len(T))*100))
	return f'{pct}%'
	
def ask(Q):
	return C.prompt(text=Q[0],type=Q[1],default=Q[2])


@C.command()
def prompt() -> None:
	
	ndisk=len(unit.fs.get_list())	
	# Q1 #########
	name=ask(Q[1])
	C.echo(name)
	C.echo()
	lib.fs.touch(f'/etc/btrwin/{name}.conf')
	unit.conf.create_new_sysconf(name)
	
	# Q2 ##########
	disk=ask(Q[2])
	while disk == 0:
		unit.fs.list()
		disk=ask(Q[2])
	unit.fs.select_disk(disk)
	unit.fs.list()
	C.echo()
	
	# Q3 ###########
	pthdsk = ask(Q[3])
	
	
	seldisk=unit.fs.get_list()[disk-1]
	mount=seldisk[1]
	unit.setup.create.sys_folders(os.path.join(mount, pthdsk))
	unit.setup.create.sys_links(os.path.join(mount, pthdsk))
	
	init={
	'file' 		:		name,
	'section'	:		'PATH',
	'config'	:		f'/etc/btrwin/{name}.conf',
	'mount'		:		mount,
	'sys'			:		'${mount}/'+ f'{pthdsk}/btrwin',
	'loaders'	:		'${sys}/loaders',
	'subv'		:		'${sys}/subv'}
	
	lib.conf.set_dict(init, G)
	unit.conf.save(G)
	
# init['subv']='${sys}/subv'sys}/subv'

#3 setup directory # init['sys']='${mount}/opt/btrwin
# '
# init['subv']='${sys}/subv'structure on mount
# default  install path  [mount]/opt/btrwin




#write [path]sys  to confing


prompt()

#create dir struct on pathsys


#store most important dirs in sysconfig




#aggregate loaders/runners to btrwin and symlink original location




