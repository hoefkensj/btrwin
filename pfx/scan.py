#!/usr/bin/env python
import os,pickle,multiprocessing
from betterwin import confctl
def walk(start, ext ,data):
	match={}
	for current, folders, files in os.walk(start, topdown=True, followlinks=False):
		ststr='drive_c'
		for file in files:
			if f'.{ext}' == file[-4:] :
				ppath = os.path.abspath(current)
				match[f'{file}']= str(ppath)
				print(f'found {file}')
			data=match
	for key in data.keys():
		print(key,data[key])
	
	#pickle.dump( data, open("./save.p", "wb" ) )

def scn_ext(basedir,ext,data):
	subv=confctl.glob['betterwin']['PATH']['subv']
	
	PTH = 	os.path.abspath(os.path.join(subv,basedir))
	proc = multiprocessing.Process(
				target=walk,
				args=(PTH, ext, data))
	proc.start(), proc.join()
	#data = pickle.load( open( "save.p", "rb" ) )
	print(data)

def main():
	scn_ext('/mnt/btrd0v1/opt/BTRWin/subv/Office/','exe',data=[])
	scn_ext('/mnt/btrd0v1/opt/BTRWin/subv/Office/','EXE',data=[])

if __name__ == '__main__':
	main()
