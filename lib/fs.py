#!/usr/bin/env python
import os
import logging
import shutil
import shlex
import re
import subprocess
import subprocess_tee
# import subprocess_tee as subprocesst

#logging.basicConfig(level=logging.INFO,filename='', format='%(message)s')
# logging.basicConfig(level=logging.WARNING,format="[%(levelname)s] %(message)s", handlers=[logging.FileHandler("created.sh"),logging.StreamHandler()])

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
	for dir in SKELL.keys():
		logging.info(f'cd {dir.format(**k)}')
		os.chdir(dir.format(**k))
		for src in SKELL[dir].keys():
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
	except FileExistsError:pass
	except FileNotFoundError:pass
	try:os.rmdir(lnk)
	except FileNotFoundError:pass
	os.symlink(src,lnk)

def touch(fname, mode=0o666, dir_fd=None, **k):
	"""
	WTF is this?  but it works the same as gnu/unix touch wich is what we needed
	"""
	flags = os.O_CREAT | os.O_APPEND
	with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
		os.utime(f.fileno() if os.utime in os.supports_fd else fname,
		dir_fd=None if os.supports_fd else dir_fd, **k)
	return os.path.abspath(fname)

def rmr(path):
	shutil.rmtree(path)

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
	ls= subs[str(arg)]
	path=os.path.abspath(path)
	pli=[os.path.join(path,it) for it in ls(path) if any(['p' in flags])]
	return pli

def ls_A(path):
	A 			=	[name for name in os.listdir(path)]
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
	
def ls_blockdev(**k) -> dict:
	"""
	:return: list of storage devices
	"""
	blockdevs={}
	cmd_lsblk_devs = 'lsblk -I 259,8 --list -o TYPE,NAME,PATH'
	result = subprocess_tee.run(cmd_lsblk_devs , tee=False)
	for row in result.stdout.split('\u000A'):
		if str(row[:4]).casefold() == 'disk'.casefold():
			blockdev={'NAME':	row[5:].split('\u0020')[0],
								'PATH':	row[5:].split('\u0020')[-1],}
			blockdevs[blockdev['NAME']]= {**blockdev}

	for blockdev in blockdevs:
		cmd_lsblk_dev=f'lsblk --pairs --all --fs --include 259,8 /dev/{blockdev}'
		result = subprocess_tee.run(cmd_lsblk_dev , tee=False)
		blockdevs[blockdev]=result.stdout.splitlines()

	named_blockdevs={}
	for blockdev, value in blockdevs.items():
		named_blockdevs[blockdev]={}
		for lst_dev in value:
			dev=lst_dev.split()[0].split('=')[1].strip('"')
			named_blockdevs[blockdev][dev]={}
			for propset in lst_dev.split():
				key = propset.split('=')[0]
				val= propset.split('=')[-1]
				if key != val:
					val =propset.split('=')[1]
					named_blockdevs[blockdev][dev][key]=val.strip('"')
	return named_blockdevs
	
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
	return sum([len(files) for r, d, files in os.walk(path)])

def cp(srcdir, dest):
	"""
	copys files form srcdir to dest, returns stdout in pipe in realtime
	:param srcdir:
	:param dest:
	:return:
	"""
	cp_cmd=shlex.split(f'cp -rvpf {srcdir} {dest}')
	proc_cp = subprocess.Popen(cp_cmd, stdout=subprocess.PIPE, universal_newlines=True)
	for line in iter(popen.stdout.readline, ""):
		yield line
	proc_cp.stdout.close()
	return_code = popen.wait()
	if return_code:
		raise subprocess.CalledProcessError(return_code, cp)

