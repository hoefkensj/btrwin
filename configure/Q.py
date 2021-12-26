import click 						as C
import os
import colorama
import types
import btrwin.configure as configure
import btrwin.lib 			as lib
import btrwin.units 		as units
import btrwin.assets		as assets

LC	= assets.locale.enUS_configure_cli
hardcoded={'PATH':{} }
hardcoded['PATH']['dir_sysconf']='/etc/btrwin/'
G=units.conf.load()
q_scheme ={
1.01_01:	[LC.Q_TEXT[1.01_01],	C.STRING,	'btrwin'],
1.02_01:	[LC.Q_TEXT[1.02_01], 	C.INT 	,	 0			],
1.03_01:	[LC.Q_TEXT[1.03_01], 	C.STRING,	'opt'		],
1.04_00:	[LC.Q_TEXT[1.04_00], 						'Y'			],
1.04_01: 	[LC.Q_TEXT[1.04_01], 	C.STRING,	''			],
}

def ns_q():
	ns_q=types.SimpleNamespace()
	def q1():
		name=configure.Q.Ask.ask(q_scheme[1.01_01])
		C.echo(f'Name: {colorama.Fore.GREEN}{name}{colorama.Style.RESET_ALL}\n')
		Exec.q1_post(name)
		return name

	def q2():
		"""
		get the currently selected disk from config if there is one
		and adjust the default answer for the Q
		and check number of valid answers for Q
		ask to select disk and select selcted disk by number
		:return: mountpoint of selected volume
		"""
		def default():
			"""
			check for prev selected disks and if still in system
			if previous disk is selected and present change the default Answer to that disks number
			:return: None
			"""
			sld=units.fs.selected_disk()
			for idx,dsk in enumerate(lib.fs.ls_disks('btrfs')):
				configure.Q.q_scheme[2][2]	= idx + 1 if sld is not None and sld in dsk[1] else configure.Q.q_scheme[2][2]
		
		default()
		disk=0
		while disk not in range(1,len(lib.fs.ls_disks('btrfs')+1)):
			disk=configure.cli.ask(configure.cli.Q[2])
			if disk == 0:
				C.echo('Detected Btrfs Volumes (mounted):')
				units.fs.list()
		units.fs.select_disk(disk)
		return units.fs.get_list()[disk-1][1]

	def q3(mount):
	
		def exec(mount,pth):
			USERHOME	=	os.environ.get('HOME')
			USER			=	os.environ.get('USER')
			PATH			=	os.path.join(mount, pth)
			units.setup.create.sys_folders(PATH)
			units.setup.create.sys_links(USERHOME=USERHOME,USER=USER,PATH=PATH)
	
		pth = configure.cli.ask(configure.cli.Q[3])
		exec(mount, pth)
		return pth

	def ns_q4():
		ns_q4=types.SimpleNamespace()
		
		def s0():
			return configure.cli.ok(configure.cli.Q[4])
	
		def s1(*a,**k):
			FPATH=f'{k["PATH"]}/{k["NAME"]}/loaders/wine'
			configure.cli.Q[41][2]=FPATH
			return configure.cli.ask(configure.cli.Q[41])
		
		def s1_copy(coldir):
			src_master=f'{os.environ.get("HOME")}/.local/share/lutris/runners/wine'
			runners=lib.fs.ls_dirs(src_master)
			for runner in runners:
				configure.cli.cpy(runner, coldir)
		
		def s1_dell(coldir):
			src_master=f'{os.environ.get("HOME")}/.local/share/lutris/runners/wine'
			runners=lib.fs.ls_dirs(src_master)
			for runner in runners:
				lib.fs.rmr(runner)
				lib.fs.rmr(os.path.split(runner)[0])
		
		ns_q4.s0=s0
		ns_q4.s1=s1
		ns_q4.s1_copy=s1_copy
		ns_q4.s1_del=s1_dell
		return ns_q4
	q4=ns_q4()
	
	ns_q.q1=q1
	ns_q.q2=q2
	ns_q.q3=q3
	ns_q.q4=q4
	return ns_q

def ns_save():
	ns_save=types.SimpleNamespace()
	
	def default(name, PATH):
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
	
	def tluafed(name, PATH):
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
	
	def init(name,mount,pth):
		sys=os.path.join('${mount}', pth,'btrwin')
		init={
	'file' 		:		name,
	'section'	:		'PATH',
	'config'	:		f'/etc/btrwin/{name}.conf',
	'mount'		:		mount,
	'sys'			:		sys ,
	'loaders'	:		'${SYS}/loaders',
	'subv'		:		'${SYS}/subv',
	}
		lib.conf.set_dict(init, G)
		units.conf.save(G)
		return units.conf.load()
		
	def dirs(name):
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
	
	def all(n,m,p):
		PATH=os.path.join(m, p)
		Gt=save_init(n,m,p)
		Gt=save_default(n,PATH)
		GT=save_tluafed(n,PATH)
		Gt=save_dirs(n)
		return Gt
	
	ns_save.all			= all
	ns_save.default	= default
	ns_save.tluafed	= tluafed
	ns_save.init		= init
	ns_save.dirs		= dirs
	return ns_save

def ns_ask():
	ns_ask= types.SimpleNamespace()
	def ask(Q):
		return C.prompt(text=Q[0],type=Q[1],default=Q[2])
	def int(Q):
		return C.prompt(text=Q[0],type=Q[1],default=int(str(Q[2])))
	def ok(Q):
		return C.confirm(text=Q[0],default=Q[1])
	ns_ask.ask= ask
	ns_ask.int= int
	ns_ask.ok = ok
	return ns_ask

def ns_exe():
	ns_exe= types.SimpleNamespace()
	def exe(Q):
		return C.prompt(text=Q[0],type=Q[1],default=Q[2])
	def int(Q):
		return C.prompt(text=Q[0],type=Q[1],default=int(str(Q[2])))
	def ok(Q):
		return C.confirm(text=Q[0],default=Q[1])
	ns_exe.exec= exe
	ns_exe.int	= int
	ns_exe.ok 	= ok
	return ns_exec

def ns_exec():
	ns_exec= types.SimpleNamespace()
	def q1_post(name):
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
			units.conf.ctl.create_new_sysconf(name)
	
	def q2_pre():
		sld=units.fs.selected_disk()
		for idx,dsk in enumerate(lib.fs.ls_disks('btrfs')):
			if sld is not None and sld in dsk[1] :
				idxsld=idx+1
				Q[2][2]=idxsld
			valid=idx+1
		return valid
	
	def q3_post(mount,pth):
		USERHOME	=	os.environ.get('HOME')
		USER			=	os.environ.get('USER')
		PATH			=	os.path.join(mount, pth)
		units.setup.create.sys_folders(PATH)
		units.setup.create.sys_links(USERHOME=USERHOME,USER=USER,PATH=PATH)
	ns_exec.q1_post=q1_post
	ns_exec.q2_pre= q2_pre
	ns_exec.q3_post	= q3_post
	
	return ns_exec

Q			=	ns_q()
Save	=	ns_save()
Ask		=	ns_ask()
Exe  =	ns_exe()
Exec	=	ns_exec()
