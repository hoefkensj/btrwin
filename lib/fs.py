#!/usr/bin/env python
import os
import logging
import shutil
import shlex
import subprocess
import subprocess_tee
import re
# import subprocess_tee as subprocesst

#logging.basicConfig(level=logging.INFO,filename='', format='%(message)s')
# logging.basicConfig(level=logging.WARNING,format="[%(levelname)s] %(message)s", handlers=[logging.FileHandler("created.sh"),logging.StreamHandler()])

def cp(srcdir, dest):
	"""
	copys files form srcdir to dest, returns stdout in pipe in realtime
	:param srcdir:
	:param dest:
	:return:
	"""
	cp_cmd=shlex.split(f'cp -rvpf {srcdir} {dest}')
	proc_cp = subprocess.Popen(cp_cmd, stdout=subprocess.PIPE, universal_newlines=True)
	yield from iter(proc_cp.stdout.readline, "")
	proc_cp.stdout.close()
	return_code = proc_cp.wait()
	if return_code:
		raise subprocess.CalledProcessError(return_code, cp)


def mkdirtree(dic, path):
	"""
	creates directory tree on disk from dictionary, at /path/
	:param dic: formatted dict,skell for dir structure
	:param path: a string with the rootpath for the structure
	:return: None
	"""
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			logging.info(f'mkdir {next_path} ...')
			os.makedirs(next_path,  exist_ok=True)
			mkdirtree(info, next_path)

def mklinktree(SKELL,**k):
	for folder in SKELL.keys():
		logging.info(f'cd {folder.format(**k)}')
		os.chdir(folder.format(**k))
		for src in SKELL[folder].keys():
			logging.info(f'ln -s {src.format(**k)} {SKELL[dir][src].format(**k)}')
			mklink(src.format(**k),SKELL[dir][src].format(**k))

def mklink(src,lnk):
	"""
	checks if link location exists and removes anything that is there
	makes symlink lnk --> src
	:param src: source for the link (what the link links to) lnk --> src
	:param lnk: name for the link: mylinkfolder -> ogfolder
	:return: None
	"""
	try:os.remove(lnk)
	except (FileExistsError, FileNotFoundError):pass
	try:os.rmdir(lnk)
	except FileNotFoundError:pass
	os.symlink(src,lnk)


def ls(path,arg,flags='p'):
	"""
	similar to unix ls flags that diffrer from the original:
	p=path=prepend path to each entry
	:param path: str(path) to ls
	:param arg: argument for ls one of  (arg : executes) :
						'all'		:	ls_A			,	'a'			:	ls_A 			,	'dirs'	:	ls_dirs		,	'd'			:	ls_dirs		,
						'files'	:	ls_files	,	'f'			:	ls_files	,	'disks'	:	ls_disks	,	'k'			:	ls_disks	,
						'pyod'	:	ls_pyod		,	'l'			:	ls_pyod		,
	:param flags: 'p' concats the abspath to every entry
	:return: contents of path as a list
	"""
	subs= {
					'all'  :	ls_A			,	'a':	ls_A 			,	'dirs':	ls_dirs		,	'd':	ls_dirs		,
					'files':	ls_files	,	'f':	ls_files	,	'disks':	ls_blockdev	, 'k':	ls_blockdev	,
					'pyod' :	ls_pyod		,	'l':	ls_pyod		,
	}
	lsfn= subs[str(arg)]
	path=os.path.abspath(path)
	pli=[os.path.join(path,it) for it in lsfn(path) if any(['p' in flags])]
	return pli

def ls_A(path):
	A = list(os.listdir(path))
	li=[]
	dirs		=	sorted([item for item in A if os.path.isdir(os.path.join(path, item))])
	li+=dirs
	files 	=	sorted([item for item in A if os.path.isfile(os.path.join(path, item))])
	li+= files
	return li

def ls_dirs(path):
	"""
	:param path: path to directory to list
	:return: list of dirs in path (/path/dir)
	"""
	return [os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def ls_files(path):
	"""
	:param path: path to directory to list
	:return: list of files in path
	"""
	try:
		f=[os.path.join(path, name) for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
	except FileNotFoundError:
		f=''
	return f
	

def ls_btrfsvol():
	pass

def ls_blockdisks(**k) -> dict:
	"""
	:return: list of storage devices
	"""
	cmd = 'lsblk' #259 = maj:NVME , 8 =maj:scsi/sata
	cmd_args_default='--include 259,8  --noheadings --all --nodeps --list -o NAME'
	lst_stdout=subprocess.run(shlex.split(f'{cmd} {cmd_args_default}'),capture_output=True,text=True,universal_newlines=True).stdout.split()

	print(lst_stdout)

def ls_blockparts(**k):
	parts=[]
	rex=re.compile('(.*?)\s')
	cmd = 'lsblk'
	cmd_args_default='--list --noheadings --all  -o NAME,LABEL,FSTYPE'
	cmd_args_disk='/dev/{}'.format(k.get('disk')) if k.get('disk') else ''
	lst_stdout=subprocess.run(shlex.split(f'{cmd} {cmd_args_default} {cmd_args_disk} '),capture_output=True,text=True,universal_newlines=True).stdout.splitlines()
	for line in lst_stdout:
		name=rex.search(line)
		if str(name[1]).startswith('nvme') and str(name[1])[-2]=='p':
			parts+=[line]
		if str(name[1])[-1].isnumeric() and not str(name[1]).startswith('nvme'):
			parts+=[line]
	return parts

def ls_blockfs(**k):
	partsfs=allfsparts=[]
	rex=re.compile('\s*([a-zA-Z0-9]*?)$')
	cmd = 'lsblk'
	cmd_args_default='--list --noheadings --all --sort FSTYPE  -o NAME,LABEL,FSTYPE'
	cmd_args_disk='/dev/{}'.format(k.get('disk')) if k.get('disk') else ''
	lst_stdout=subprocess.run(shlex.split(f'{cmd} {cmd_args_default}'),capture_output=True,text=True,universal_newlines=True).stdout.splitlines()
	# for line in lst_stdout:
	# 	print(str(rex.search(line)[1]))
	partsfs= [line for line in lst_stdout if str(rex.search(line)[1]) == k.get('fs')]
	allfsparts=[line for line in lst_stdout if str(rex.search(line)[1])]
	return partsfs if k.get('fs') else allfsparts
	
def ls_blockfs_btrfs():
	blockfs_btrfs=ls_blockfs(fs='btrfs')
	for line in blockfs_btrfs:
		print(line)


def ls_pyod(path, flags=''):
	"""
	similar to the systems 'ls -A' lists directory contents
	:param path full system path of the dir to ls
	:return: the contents of the dir split in [python scripts], [other], [dirs]
	"""
	A 			=	[name for name in os.listdir(path)]
	visible	=	[item for item in A if not item.startswith('.')]
	pyscrs	=	sorted([item for item in visible if item.endswith('.py')], key=str.casefold)
	dirs		=	sorted([item for item in visible if os.path.isdir(os.path.join(path, item))])
	dirs 		=	[d for d in dirs if not d.startswith('__')]
	other 	=	sorted([item for item in visible if item not in dirs and item not in pyscrs])
	other 	=	[o for o in other if not o.startswith('__')]
	return 		[pyscrs,other,dirs]
	



def renumerate(path):
	return sum(len(files) for r, d, files in os.walk(path))

def rmr(path):
	shutil.rmtree(path)

def touch(fname, mode=0o666, dir_fd=None, **k):
	"""
	WTF is this?  but it works the same as gnu/unix touch wich is what we needed
	"""
	flags = os.O_CREAT | os.O_APPEND
	with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
		os.utime(f.fileno() if os.utime in os.supports_fd else fname,
		dir_fd=None if os.supports_fd else dir_fd, **k)
	return os.path.abspath(fname)

# [print(part) for part in ls_blockfs(fs='')]
ls_blockfs_btrfs()