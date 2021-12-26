#!/usr/bin/env python
import os
import time
import types
import click as C

import btrwin.assets 	as assets
import btrwin.configure as configure
import btrwin.lib as lib
import btrwin.units as units

LC	= assets.locale.enUS_configure_cli

Q= configure.Q.Q
Save=configure.Q.Save
Ask=configure.Q.Ask
Q = configure.Q.Q
Exe=configure.Q.Exe
Exec=configure.Q.Exec


cp=lib.fs.cp
G=units.conf.load
types.SimpleNamespace()

LC.Q_TEXT

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
	
def Q1():
	name=Ask.ask(Q[1])
	C.echo(f'Name: {Fore.GREEN}{name}{Style.RESET_ALL}\n')
	Exec.q1_post(name)
	return name

def Q2():
	# get the currently selected disk from config if there is one
	# and adjust the default answer for the Q
	# and check number of valid answers for Q
	valid=Exec.q2_pre()
	disk=0
	while disk not in range(1,valid+1):
		disk=ask(Q[2])
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			units.fs.list()
	units.fs.select_disk(disk)
	return units.fs.get_list()[disk-1][1]
	
def Q3(mount):
	pth = ask(Q[3])
	Exec.q3_post(mount,pth)
	return pth

def Q4():
	return yes(Q[4])

@C.command()
def prompt() -> None:
	G=units.conf.load
	ndisk=len(units.fs.get_list())
	
	# SEQ PART1 ########
	name=Q.q1()
	mount=Q.q2()
	pth=Q.q3(mount)
	G=Save.all(name,mount, pth)

	# SEQ PART2 ########

	if Q.q4.s0():
		known_wine= units.setup.known.wine_locs
		wloc=[known_wine[key].format(USERHOME	=	os.environ.get('HOME')) for key in known_wine]
		wldrs=[lib.fs.ls_dirs(d) for d in wloc if os.path.exists(d) ]
		wine_ldrs=Q.q4.s1(PATH=pth,NAME=name)
		if wldrs:
			Q.q4.s1_copy(wine_ldrs)
			Q.q4.s1_del(wine_ldrs)
			Q41_lns('{parents}')

prompt()

#create dir struct on pathsys


#store most important dirs in sysconfig




#aggregate loaders/runners to btrwin and symlink original location


