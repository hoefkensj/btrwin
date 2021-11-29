#!/usr/bin/env python
import os,pickle,multiprocessing,subprocess
from os import path as op
from conf import G
G=G()

BTW=G['betterwin']
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
	entries=[]
	#CFG=G[PFX]						#PREFIX CONFIG
	#PPFX=CFG['PATH']['path']		#PREFIX PATH
	if PFX == 'default':
		PPFX= f"{os.environ['HOME']}/.wine"
	PFXC=op.join(PPFX,'drive_c')		#PREFIX DRIVE_C
	EXT=['exe','lnk']					#extentions to look for
	for current,folders,files in os.walk(PFXC, topdown=True ,followlinks=False):
		for f in files:
			if EXT[0] in f[-4:]:
				for idx,folder in enumerate(current.split('/')):
					if folder == 'drive_c':
						strt=idx+1
						break
						c=current[strt:]
						c.reverse()
			
			
				entries+=(f,c)
	
		for entry in entries:
			print(f'{entry}\n')
		
		
		
		
		#print([[f,current] for f in files if EXT[0] in f[-4:] ])
		

def scan(PFX):
	proc = multiprocessing.Process(
				target=step,
				args=(PFX))
	proc.start(), proc.join()
	

	
	
def main(pfx):
	scan(pfx)

if __name__ == '__main__':
	main(['default'])

