#!/usr/bin/env python
import btrwin.lib 	as	 lib
import sys
import os

from lib.fs import ls_pyod

pkg=lib.dev.pkg

find_master		=		pkg.find_master
is_pkg				=		pkg.is_pkg

ls					= ls_pyod
ls_dir			=			lib.fs.ls_dirs
ls_files		=			lib.fs.ls_files
sprint			=			sys.stdout.write
get_master	=			lib.dev.pkg.find_master
ls					= ls_pyod
def lsR(cd):
	dirs_nodots=[d for d in ls_dir(cd) if not os.path.split(d)[1].startswith('.')]
	dirs_nodots_nopycache=[d for d in ls_dir(dirs_nodots) if not os.path.split(d)[1].startswith('.')]
	pyscrs_all=[]
	pyp1=[]

	for fol2 in d_l1:
		path0=os.path.join(fol,fol2)

		d_l2=[d for d in ls_dir(os.path.join(fol,fol2)) if not  os.path.split(d)[1].startswith('.')]
		pys,_,_=ls(d_l2)
		for file  in pys:
			pyp1=os.path.join(fol,file)
		pyscrs_all+=pyp1
		
		# for d2 in ds1:
		# 	pys=ls(d2)[0]
		# 	for file  in pys:
		# 		pyp2=os.path.join(d2,file)
		# 	pyscrs_all+=pyp2
		
		
	lsR(os.path.join(path0,d2))
	
	
	return pyscrs_all

def ls_py(path):
	pyscrs,other,dirs=ls(path)
	print(pyscrs)

if __name__ == '__main__':
	print(lsR(find_master()))
	print(find_master())