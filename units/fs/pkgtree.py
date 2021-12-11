import os,sys

sprint=sys.stdout.write

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

def ispkg(dirpath):
	"""
	:param dirpath: path to test for it being a python package (has __init__.py)
	:return: boolean (true for is package false if not )
	# True if True in [True for item in os.listdir(dirpath) if  item == "__init__.py" ] else False =>>>
	# test = any([True for item in os.listdir(dirpath) if  item == "__init__.py" ]) =>>>
	"""
	return any(["__init__.py" in os.listdir(dirpath)])

def get_master():
	"""
	!!! warning breaks when __init__. is in everyfolder of the path up until /  !!!
	gets the folder(path) that is the highest up in the path that still is a python package
	"""
	pathself=sys.argv[0]
	pself=pathself
	parent_dir_pself=os.path.split(pself)[0]
	pdirps=parent_dir_pself
	lst_parent_folders_pself = pdirps.split('/')
	lst_pdps=lst_parent_folders_pself
	os.chdir(os.path.split(sys.argv[0])[0])
	return [pkg[0] for pkg in ([path,ispkg(path) ] for path in  ['/'.join(lst_pdps[:(len(lst_pdps)-idx)]) for idx, folder in enumerate(reversed(lst_pdps)) if os.path.exists('/'.join(lst_pdps[:(
		len(lst_pdps)-idx)]))][:-1])if pkg[1] == True][-1]

def tabs(n):
	return (n*'    ')

def level(n):
	#special case:
	level0=tabs(1)
	if n==0:
		return f'{level0}'

	lvl=f'{tabs(1)}'
	lvls=n*lvl
	prefix=f'{tabs(1)}{lvls}'
	return prefix

def ismodule(path):
	if '.py' == path[:-3]:
		pass
	# utopia would test the file contents for the first line being #! to python
	return True if True in [True for item in os.listdir(path) if  item == "__init__.py" ] else False

def ffix(ftype):
	case    = { 'f': '|--< ',
							'd': '|--[/] '}
	return case[ftype]

def build_tree():
	pkgpath = get_master()
	pkgname = os.path.split(pkgpath)[-1]
	# contents = os.listdir(path)
	
	def get_contents(path):
		sall = ls(path)
		return sall[0], sall[1], sall[2]
	
	def sprint_files(path,childof):
		prefix=f'    {childof}{ffix("f")}'
		for file in get_contents(path)[0]:
			sprint(f'{prefix}{file}\n')
		for file in get_contents(path)[1]:
			sprint(f'{prefix}{file}\n')
		#sprint(f'{childof}|\n')
		
	def sprint_folder(path, childof, thisfolder):
		sprint(f'{childof}{ffix("d")}{thisfolder}\n')
		sprint_files(path, childof)
		childof += '|   '

		for idx, folder in enumerate(get_contents(path)[2]):
			sprint_folder(os.path.join(path,folder),childof,folder)
		#sprint(f'{childof}\n')
		# prefix=get_prefix('f',lvl+1)
		# sprint_pyscr(path,prefix)
		# sprint_other(path, prefix)


	sprint(f'\n#==>[~]\t\"\"\"\tPackage: [ \'{pkgname}\' ]\t\"\"\"')
	sprint(f'\n     |')
	sprint(f'\n')
	path = pkgpath
	sprint_folder(pkgpath,"     ",pkgname)

def main(pfx):
	build_tree()
	
if __name__ == '__main__':
	main()

