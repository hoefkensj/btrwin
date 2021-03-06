#!/usr/bin/env python
import os
import argparse
import lib 	as lib
import fnx as units


#G=fnx.conf.load()

def create_prefix_config(PREFIX,TPL='',BIT='',EXES=''):
	G=fnx.conf.load()
	bin=['wine','wine64','wineboot','winecfg','wineconsole','msiexec','notepad','regedit','regsvr32','wineserver','winepath',]
	PFX= os.path.join(G['btrwin']['PATH']['subv'], PREFIX)
	EXES= '${path}'+f'/{EXES}'
	LDR_BIN='${PATH:ldrbin}'
	BIT= G[TPL]['WINE_ENV']['BIT']
	
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
 
	lib.conf.set_dict(PATH)
	lib.conf.set_dict(WINE_ENV)
	lib.conf.set_dict(WINE_BIN)




def main():
	a=getargs()
	create_prefix_config(a.PREFIX,a.BIT,a.EXES)

if __name__ == '__main__':
	main()
