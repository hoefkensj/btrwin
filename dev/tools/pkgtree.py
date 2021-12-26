#!/usr/bin/env python
import os
import sys
import btrwin.lib as lib

pkg=lib.dev.pkg

find_master		=		pkg.find_master
is_pkg				=		pkg.is_pkg
is_mod				=		pkg.is_module

def tabs(n):
	return (n*'    ')

def ffix(ftype):
	case    = { 'f': '|--< ',
							'd': '|--[/] '}
	return case[ftype]

def build_tree():
	pkgpath = find_master()
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

def main():
	build_tree()
	
if __name__ == '__main__':
	main()

