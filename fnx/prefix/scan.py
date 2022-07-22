#!/usr/bin/env python
import os, multiprocessing
from os import path as op
from modules import conf

G= conf.G()
BTW=G['btrwin']
SVL=BTW['PATH']['subv']

def walk(start, ext ,data):
	match={}
	for current, folders, files in os.walk(start, topdown=True, followlinks=False):
		ststr='drive_c'
		for file in files:
			if f'.{ext}' == file[-4:] :
				ppath = op.abspath(current)
				match[f'{file}']= str(ppath)
				print(f'found {file}')
			data=match
	for key in data.keys():
		print(key,data[key])

	#pickle.dump( data, open("./save.p", "wb" ) )
	
def step(PFX):
	global G
	lib={}
	pathrev=path=[]
	#CFG=G[PFX]						#PREFIX CONFIG
	#PPFX=CFG['PATH']['path']		#PREFIX PATH
	if PFX == 'default':
		PPFX= f"{os.environ['HOME']}/.wine"
	PFXC=op.join(PPFX,'drive_c')		#PREFIX DRIVE_C
	EXT=['exe','lnk']					#extentions to look for
	for current,folders,files in os.walk(PFXC, topdown=True ,followlinks=False):
		for f in files:
			if EXT[0] in f[-4:]:
				c=current.split('/')
				for d in c:
					check=c.pop(0)
					if 'drive_c' in check:
						path=c
						for dir in path :
							[pathrev]=[[d]+[pathrev]]
							entry=[f,[path,pathrev]]
							lib[f]= entry
	for exe in lib:
		print(lib[exe])

def scan(PFX):
	proc = multiprocessing.Process(
				target=step,
				args=(PFX))
  proc.start(), proc.join()

def main(pfx):
	scan(pfx)

if __name__ == '__main__':
	main(['default'])

