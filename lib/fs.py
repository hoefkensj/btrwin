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
					'files':	ls_files	,	'f':	ls_files	,	'disks':	ls_blkdisks	, 'k':	ls_blkdisks	,
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

def ls_dirs(path,**k):
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

def ls_blk(**k):
	cmd = 'lsblk'
	cmd_args_default='--list --noheadings --all'
	cmd_opts=k.get('opts') if k.get('opts') else ''
	cmd_line=f'{cmd} {cmd_args_default} {cmd_opts}'#.format(cmd=cmd,cmd_args_default=cmd_args_default,cmd_opts=cmd_opts)
	lst_cmdline=shlex.split(cmd_line)
	return subprocess.run(lst_cmdline,capture_output=True,text=True,universal_newlines=True)

def ls_blkdisks(**k) -> dict:
	"""
	:return: list of storage devices
	"""
	cmd_opts='--include 259,8 --nodeps -o NAME'#259 = maj:NVME , 8 =maj:scsi/sata
	return ls_blk(opts=cmd_opts).stdout.splitlines()

def ls_blkparts(**k):
	cmd_args_disk='/dev/{}'.format(k.get('disk')) if k.get('disk') else ''
	cmd_opts=f'-o TYPE,NAME {cmd_args_disk}'
	lst_stdout=ls_blk(opts=cmd_opts).stdout.splitlines()
	parts=[line.split()[1] for line in lst_stdout if line.split()[0]=='part']
	return parts


def ls_blkfs(**k):
	rex=re.compile('\s*([a-zA-Z0-9]*?)$')
	partsfs=allfsparts=[]
	cmd_args_disk='/dev/{}'.format(k.get('disk')) if k.get('disk') else ''
	cmd_opts=f'--sort FSTYPE -o NAME,FSTYPE {cmd_args_disk}'
	lst_stdout=ls_blk(opts=cmd_opts).stdout.splitlines()
	partsfs= [line.split()[0] for line in lst_stdout if str(rex.search(line)[1]) == k.get('fs')]
	allfsparts=[line for line in lst_stdout if str(rex.search(line)[1])]
	return partsfs if k.get('fs') else allfsparts

# print(ls_blkfs(disk='nvme1n1',fs='ntfs'))

def ls_fs_btrfs():
	sys_btrfs='/sys/fs/btrfs/'
	if os.path.isdir(sys_btrfs):
		btrfs_vols=ls_dirs(sys_btrfs)
		btrfs_vols= [os.path.join(sys_btrfs,vol) for vol in btrfs_vols if vol!= os.path.join(sys_btrfs,'features')]
		btrfs_devs=[]
		for vol in btrfs_vols:
			devices=[os.path.split(dev)[1] for dev in  ls_dirs(os.path.join(vol,'devices'))]
			if os.path.isfile(os.path.join(vol,'label')):
				with open(os.path.join(vol,'label'),'r') as label:
					label=label.read().strip()
			else:
				label='!!NOLABEL!!'
			dev=[label,os.path.split(vol)[1],devices]
			btrfs_devs+=[dev]
	return btrfs_devs

# def ls_blk_mounts():

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

