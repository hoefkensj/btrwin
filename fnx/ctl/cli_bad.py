#!/usr/bin/env python
import os
import types

import click as C
import colorama as col
import btrwin.assets as assets
import btrwin.lib as lib
import fnx.check.ctl
import fnx.file.ctl
import fnx.fs.ctl

Q = types.SimpleNamespace()

cp = lib.fs.cp

LC = assets.static.locale.enUS_configure_cli

Q.scheme = {
	.00_01: [LC.Q_TEXT[.00_01], 'Y'],
	.01_01: [LC.Q_TEXT[.01_01], C.STRING, 'btrwin'],
	.02_01: [LC.Q_TEXT[.02_01], C.INT, 0],
	.03_01: [LC.Q_TEXT[.03_01], C.STRING, 'opt'],
	.04_00: [LC.Q_TEXT[.04_00], 'Y'],
	.04_01: [LC.Q_TEXT[.04_01], C.STRING, ''],
}
scheme ={
	.01_01:	[LC.Q_TEXT[.01_01],		C.STRING,	'btrwin'],
	.02_01:	[LC.Q_TEXT[.02_01], 	C.INT 	,	 0			],
	.03_01:	[LC.Q_TEXT[.03_01], 	C.STRING,	'opt'		],
	.04_00:	[LC.Q_TEXT[.04_00], 						'Y'			],
	.04_01: [LC.Q_TEXT[.04_01], 	C.STRING,	''			],
}


def Q0201_set_default_disk():
	"""
	check for prev selected disks and if still in system
	if previous disk is selected and present change the default Answer to that disks number
	:return: None
	"""
	sld = fnx.fs.selected_disk()
	for idx, dsk in enumerate(lib.fs.ls_blockdev('btrfs')):
		Q.scheme[1.02_01][2] = idx + 1 if sld is not None and sld in dsk[1] else Q.scheme[1.02_01][2]
	disk = 0
	while disk not in range(1, len(lib.fs.ls_blockdev('btrfs'))):
		disk = fnx.configure.Q.Ask(fnx.configure.cli_bad.Q[2])
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			fnx.fs.list()
	fnx.fs.ctl.fs_select_set(disk)
	return fnx.fs.get_list()[disk - 1][1]


# def cpy(srcdir, dest) -> None:
# 	"""
# 	copy progress
# 	"""
# 	i = 0
# 	cur = 0
# 	cpt = sum([len(files) for r, d, files in os.walk(srcdir)])
# 	pct = (cpt / 100)
#
# 	with C.progressbar(label=f"Copying {os.path.split(srcdir)[1]}", length=cpt, show_eta=False) as bar:
# 		for path in cp(srcdir, dest):
# 			cur = cur + 1 if i == pct else cur
# 			i = +1
# 			bar.update(cur)
# 			time.sleep(0.0005)
# 			pass


def save(section):
	save = fnx.conf.save
	load = fnx.conf.load
	save(lib.conf.set_dict(section, load()))


def s_all(n, m, p):
	PATH = os.path.join(m, p)
	Gt = save(init(n, m, p))
	Gt = save(default(n, PATH))
	Gt = save(tluafed(n, PATH))
	Gt = save(dirs(n))
	return Gt
	

def ask(Q):
	return C.prompt(text=Q[0], type=Q[1], default=Q[2])


def qint(Q):
	return C.prompt(text=Q[0], type=Q[1], default=int(str(Q[2])))


def ok(Q):
	return C.confirm(text=Q[0], default=Q[1])



	
	
def q2():
	"""
	get the currently selected disk from config if there is one
	and adjust the default answer for the Q
	and check number of valid answers for Q
	ask to select disk and select selcted disk by number
	:return: mountpoint of selected volume
	"""

	# get the currently selected disk from config if there is one
	# and adjust the default answer for the Q
	# and check number of valid answers for Q



def q3(mount):

	return pth

def q4(pth, name):
	def s0():
		return ok(Q.scheme[.04_00])

	def s1(*a, **k):
		FPATH = f'{k["PATH"]}/{k["NAME"]}/loaders/wine'
		Q.scheme[.04_01][2] = FPATH
		return ask(Q.scheme[.04_01])

	if s0():
		known_wine = fnx.setup.runner_paths.wine_locs
		wloc = [known_wine[key].format(USERHOME=os.environ.get('HOME')) for key in known_wine]
		wldrs = [lib.fs.ls_dirs(d) for d in wloc if os.path.exists(d)]
		wine_ldrs = s1(PATH=pth, NAME=name)
		if wldrs:
			portal()
	return

@C.command()
def prompt() -> None:
	# SEQ PART1 ########
	name = ask(Q.scheme[.01_01])
	fnx.configure.ctl.create_name(name)
	sys_conf = fnx.conf.load_sys()
	sys_conf['btrwin']['DEFAULT']['NAME']=name
	C.echo(f'Name: {col.Fore.GREEN}{name}{col.Style.RESET_ALL}\n')

	Q.scheme[.02_01][2] = fnx.file.ctl.default_disk()
	valid = fnx.check.ctl.detect_disk()
	disk = 0
	while disk not in range(1, valid + 1):
		disk = qint(Q.scheme[.02_01])
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			fnx.fs.list()
	fnx.fs.ctl.fs_select_set(disk)
	mount=fnx.fs.get_list()[disk - 1][1]
	
	pth = ask(Q.scheme[.03_01])
	fnx.file.ctl.setup_sys(mount, pth)
	
	G = s_all(name, mount, pth)
	# SEQ PART2 ########
	tmp = q4(pth=pth, name=name)

prompt()

# create dir struct on pathsys


# store most important dirs in sysconfig


# aggregate loaders/runners to btrwin and symlink original location
