import os
import click as C
from colorama import Fore, Style
from configure.cli import Q, ask, ok, cpy
import btrwin.lib as lib
import btrwin.units as units
hardcoded={'PATH':{} }
hardcoded['PATH']['dir_sysconf']='/etc/btrwin/'


def Q2_default():
	"""
	check for prev selected disks and if still in system
	if previous disk is selected and present change the default Answer to that disks number
	:return: None
	"""
	sld=units.fs.selected_disk()
	for idx,dsk in enumerate(lib.fs.ls_disks('btrfs')):
		Q[2][2]	=	idx+1 if sld is not None and sld in dsk[1] else Q[2][2]

def Q3_exec(mount,pth):
	USERHOME	=	os.environ.get('HOME')
	USER			=	os.environ.get('USER')
	PATH			=	os.path.join(mount, pth)
	units.setup.create.sys_folders(PATH)
	units.setup.create.sys_links(USERHOME=USERHOME,USER=USER,PATH=PATH)

def Q1():
	name=ask(Q[1])
	C.echo(f'Name: {Fore.GREEN}{name}{Style.RESET_ALL}\n')
	Q1_exec(name)
	return name

def Q2():
	"""
	get the currently selected disk from config if there is one
	and adjust the default answer for the Q
	and check number of valid answers for Q
	ask to select disk and select selcted disk by number
	:return: mountpoint of selected volume
	"""
	Q2_default()
	disk=0
	while disk not in range(1,len(lib.fs.ls_disks('btrfs')+1):
		disk=ask(Q[2])
		if disk == 0:
			C.echo('Detected Btrfs Volumes (mounted):')
			units.fs.list()
	units.fs.select_disk(disk)
	return units.fs.get_list()[disk-1][1]

def Q3(mount):
	pth = ask(Q[3])
	Q3_exec(mount, pth)
	return pth

def Q4():
	return ok(Q[4])


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