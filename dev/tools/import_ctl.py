#!/usr/bin/env python
import sys
import os
import colorama
import btrwin.lib as lib
import btrwin.dev as dev

Fore				=			colorama.Fore
Style				=			colorama.Style

pkg					=			lib.dev.pkg




def lsR(cd,pyscrs_all):
	dirs_nodots=[d for d in lib.fs.ls_dirs(cd) if not os.path.split(d)[1].startswith('.')]
	dirs_nodots_nopycache=[d for d in dirs_nodots if not os.path.split(d)[1]=='__pycache__']
	pyscrs_all+= [os.path.join(cd, file) for file in lib.fs.ls_files(cd) if pkg.is_module(file) or 'py' in file]
	
	for dir in dirs_nodots_nopycache:
		lsR(dir,pyscrs_all)
	return pyscrs_all

	# for fol2 in d_l1:
	# 	path0=os.path.join(fol,fol2)
	#
	# 	d_l2=[d for d in ls_dir(os.path.join(fol,fol2)) if not  os.path.split(d)[1].startswith('.')]
	# 	pys,_,_=ls(d_l2)
	# 	for file  in pys:
	# 		pyp1=os.path.join(fol,file)
	# 	pyscrs_all+=pyp1
		
		# for d2 in ds1:
		# 	pys=ls(d2)[0]
		# 	for file  in pys:
		# 		pyp2=os.path.join(d2,file)
		# 	pyscrs_all+=pyp2
		
		
	# lsR(os.path.join(path0,d2))
	
	

def ls_py(path):
	pyscrs,other,dirs=ls(path)
	print(pyscrs)


def show(cd='.'):
	path=pkg.find_master()
	all_py=lsR(path,[])
	lines=[]
	bpath=path.split('/')
	newfile=True
	files=[]
	for idx,py in enumerate(all_py):
		filenr=idx+1
		#print(py,':\t')
		shortpath= os.path.join('.','/'.join([d for d in py.split('/') if d not in bpath]))
		lines+=[f'{filenr}\t:\t{shortpath}']
		files+=[[f'{filenr}\t{shortpath}'],]
		n=0
		s=0
		i=0
		with open(py,'r') as f:
			started=False
			#lines+=[f.readline()]
			while True:
				i+=1
				line=f.readline().strip()

				if line.startswith('#!') :
					files[idx] += [f'\t{Fore.LIGHTBLACK_EX}{line.strip()}{Style.RESET_ALL}']
					s+=1
					started=True
					newfile=False
				
				if newfile:
					files[idx]+=[f'{Fore.RED}[WARNING]{Style.RESET_ALL} : #! MISSING']
					newfile=False
					
				if 'import' in line:
					nline=[]
					for item in line.strip().split(' '):
						if item == 'from':
							nitem=f'{Fore.LIGHTBLUE_EX}{item}{Style.RESET_ALL}'
						elif item == 'import':
							nitem=f'{Fore.BLUE}{item}{Style.RESET_ALL}'
						elif item == 'as':
							nitem=f'{Fore.GREEN}{item}{Style.RESET_ALL}'
						else:
							nitem=item
						nline+=[nitem]
					files[idx] += [f'\t|-{i+1}: {" ".join(nline)}']
					
					#print('\t',line.strip())
				
				
				if not line:
					break
	for f in files:
	# nlines+=[f'{[line for line in nline]}{Style.RESET_ALL}']
		if '__init__' in f[0]:
			for l in f:
				print(l)
	for f in files:
	# nlines+=[f'{[line for line in nline]}{Style.RESET_ALL}']
		if '__init__' not in f[0]:
			for l in f:
				print(l)

	
if __name__ == '__main__':
	show()
	print(pkg.find_master())