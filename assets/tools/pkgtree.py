#!/usr/bin/env python
import os
import sys
import btrwin.lib as lib
sprint=sys.stdout.write

pkg=lib.dev.pkg

find_master		=		pkg.find_master
is_pkg				=		pkg.is_pkg
is_mod				=		pkg.is_module

def tabs(n):
	return (n*'    ')

def ffix(ftype):
	case    = { 'f': '┣━ ',
              'd': '╋━[/] '}
	return case[ftype]


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
	
	
def ls_A(path):
	A = list(os.listdir(path))
	li=[]
	dirs		=	sorted([item for item in A if os.path.isdir(os.path.join(path, item))])
	li+=dirs
	files 	=	sorted([item for item in A if os.path.isfile(os.path.join(path, item))])
	li+= files
	return li

def build_tree():
	pkgpath = find_master()
	pkgname = os.path.split(pkgpath)[-1]
	# contents = os.listdir(path)
	
	def get_contents(path):
		sall = ls_pyod(path)
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
		childof += '│   '

		for idx, folder in enumerate(get_contents(path)[2]):
			sprint_folder(os.path.join(path,folder),childof,folder)
		#sprint(f'{childof}\n')
		# prefix=get_prefix('f',lvl+1)
		# sprint_pyscr(path,prefix)
		# sprint_other(path, prefix)


	sprint(f'\n#==>[~]\t\"\"\"\tPackage: [ \'{pkgname}\' ]\t\"\"\"')
	sprint(f'\n     ║')
	sprint(f'\n')
	path = pkgpath
	sprint_folder(pkgpath,"     ",pkgname)

def main():
	build_tree()
	
if __name__ == '__main__':
	main()

