#!/usr/bin/env python
import os
from btrwin.units import conf 
import argparse

C=conf.get()



def create_prefix_config(PREFIX,TPL='',BIT='',EXES=''):
	bin=['wine','wine64','wineboot','winecfg','wineconsole','msiexec','notepad','regedit','regsvr32','wineserver','winepath',]
	PFX= os.path.join(C['btrwin']['PATH']['subv'],PREFIX)
	EXES= '${path}'+f'/{EXES}'
	LDR_BIN='${PATH:ldrbin}'
	BIT= C[TPL]['WINE_ENV']['BIT']
	
	PATH =	{
		'file'					:	f'{PREFIX}'	,
		'section'				:	'PATH',
		'path'			:			f'{PFX}',
		'loader'		:			'${path}/loader',
		'exes'			:			EXES,
		'meta'			:			'${path}/meta',
		'ldrbin'		:			'${loader}/bin',
		'pfxbin'		:			'${meta}/bin',
		'exec'			:			'${meta}/exec',
		'ico'			:			'${meta}/lib/ico',
			}
	
	WINE_ENV = {
		'file'					:	f'{PREFIX}'	,
		'section'				:	'WINE_ENV',
		'WINEDEBUG' 			: 	'-all',
		'BIT'			:			f'{BIT}',
		'WINEARCH'				:	f'win{BIT}',
		'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
		'WINEPREFIX' 			:	f'{PFX}',
		'WINE'					:	f'{LDR_BIN}/wine',		
		'WINELOADER'			:	f'{LDR_BIN}/wine',
		'WINESERVER'			:	f'{LDR_BIN}/wineserver'
		}

	WINE_BIN ={
		'file'					:	f'{PREFIX}'	,
		'section'				:	'WINE_BIN',	}
	
	WINE_BIN={**WINE_BIN,**{b.upper() : f'{LDR_BIN}/{b}' for b in bin}}
 
	confctl.set_dict(PATH)
	confctl.set_dict(WINE_ENV)
	confctl.set_dict(WINE_BIN)

def getargs(): #get arguments from commandline
	parser=argparse.ArgumentParser()
	parser.add_argument('PREFIX', help='name of the prefix')
	parser.add_argument('BIT', type=str ,help='WINE ARCH')
	parser.add_argument('--EXES', type=str ,help='space " "-less folder With EXES')
	args = parser.parse_args()
	return args


def main():
	a=getargs()
	create_prefix_config(a.PREFIX,a.BIT,a.EXES)

if __name__ == '__main__':
	main()
