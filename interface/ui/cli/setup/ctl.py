#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import os

import click as C
import fnx.check
import fnx.conf
import fnx.file
import fnx.fs
import lib as lib


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
	fnx.conf.ctl.select_disk(disk)
	return fnx.fs.get_list()[disk - 1][1]
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

def q_ask(Q):
	return C.prompt(text=Q[0], type=Q[1], default=Q[2])
def q_int(Q):
	return C.prompt(text=Q[0], type=Q[1], default=int(str(Q[2])))
def q_yes(Q):
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
	fnx.conf.ctl.select_disk(disk)
	mount=fnx.fs.get_list()[disk - 1][1]
	
	pth = ask(Q.scheme[.03_01])
	fnx.file.ctl.setup_sys(mount, pth)
	
	G = s_all(name, mount, pth)
	# SEQ PART2 ########
	tmp = q4(pth=pth, name=name)