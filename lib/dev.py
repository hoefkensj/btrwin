#!/usr/bin/env python
import sys
import os
import types
sprint		=	sys.stdout.write



def pkg():
	def is_module(path):
		l=path
		try:
			with open(path,'r') as f:
				l=f.readline()
			ismod= True if l.startswith('#!') and 'python' in l else False
		except IsADirectoryError:
			ismod=False
		#True if True in [True for item in os.listdir(path) if  item == "__init__.py" ] else False
		return ismod
	def is_pkg(path):
		"""
		:param path: path to test for it being a python package (has __init__.py)
		:return: boolean (true for is package false if not )
		# True if True in [True for item in os.listdir(dirpath) if  item == "__init__.py" ] else False =>>>
		# test = any([True for item in os.listdir(dirpath) if  item == "__init__.py" ]) =>>>
		"""
		return any(["__init__.py" in os.listdir(path)])
	def find_master():
		"""
		!!! warning breaks when __init__. is in everyfolder of the path up until /  !!!
		gets the folder(path) that is the highest up in the path that still is a python package
		"""
		pathself					=	sys.argv[0]
		pself							=	pathself
		parent_dir_pself	=	os.path.split(pself)[0]
		pdirps						=	parent_dir_pself
		lst_parent_folders_pself = pdirps.split('/')
		lst_pdps=lst_parent_folders_pself
		os.chdir(os.path.split(sys.argv[0])[0])
		return [pkg[0] for pkg in ([path,pkg.is_pkg(path) ] for path in  ['/'.join(lst_pdps[:(len(lst_pdps)-idx)]) for idx, folder in enumerate(reversed(lst_pdps)) if os.path.exists('/'.join(lst_pdps[:(
			len(lst_pdps)-idx)]))][:-1])if pkg[1] == True][-1]
	pkg=types.SimpleNamespace()
	pkg.is_module		=	is_module
	pkg.is_pkg			=	is_pkg
	pkg.find_master	=	find_master
	return pkg
pkg=pkg()
