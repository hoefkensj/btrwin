#!/usr/bin/env python
import os,logging
import subprocess_tee as sproc

#logging.basicConfig(level=logging.INFO,filename='', format='%(message)s')
logging.basicConfig(level=logging.INFO,format="[%(levelname)s] %(message)s", handlers=[logging.FileHandler("created.sh"),logging.StreamHandler()])

def mkdirtree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			logging.info(f'mkdir {next_path} ...')
			os.makedirs(next_path,  exist_ok=True)
			mkdirtree(info, next_path)

def mklinktree(LINKS,path):
	for folder in LINKS:
		path=path
		logging.info(f'cd {folder}')
		os.chdir(folder)
		for link in LINKS[folder]:
			logging.info(f'ln -s {link[0]} {link[1]}')
			mklink(link[0],link[1])

def mklink(src,lnk):
		"""
		checks if link locaation exists and removes anything that is there
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



def ls(path,flags=''):
	"""
	similar to the systems 'ls -A' lists directory contents
	:param path full system path of the dir to ls
	:return: the contents of the dir split in python scripts other dirs
	"""
	A = [name for name in os.listdir(path)]	#dont concat the path to the files for now
	visible = [item for item in A if not item.startswith('.')]
	pyscrs =  sorted([item for item in visible if item.endswith('.py')], key=str.casefold)
	dirs = sorted([item for item in visible if os.path.isdir(os.path.join(path, item))])
	dirs =  [d for d in dirs if not d.startswith('__')]
	other = sorted([item for item in visible if item not in dirs and item not in pyscrs])
	other = [o for o in other if not o.startswith('__')]
	return [pyscrs,other,dirs]


def touch(fname, mode=0o666, dir_fd=None, **k):
	flags = os.O_CREAT | os.O_APPEND
	with os.fdopen(os.open(fname, flags=flags, mode=mode, dir_fd=dir_fd)) as f:
		os.utime(f.fileno() if os.utime in os.supports_fd else fname,
		dir_fd=None if os.supports_fd else dir_fd, **k)


def ls_dirs(path):
	"""
	:param path: path to directory to list
	:return: list of dirs in path
	"""
	return [os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]


def ls_files(path):
	"""
	:param path: path to directory to list
	:return: list of files in path
	"""
	return [os.path.join(path, name) for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]


def ls_disks(type):
	split=[]
	result = sproc.run("lsblk -I 259,8 --list -o FSTYPE,PATH,MOUNTPOINT,LABEL |awk '$1==\"btrfs\" {print $2,$4,$3}'| awk '$3 != \"\" {print $1, $3,$2 }'", tee=False)
	resultsplit = result.stdout.strip().split('\n')
	for line in resultsplit:
		split+=[line.split()]
	return split

