#!/usr/bin/env python
f_wine="/home/hoefkens/.wine/.meta/etc/vars_wine.conf"
f_pfx="/home/hoefkens/.wine/.meta/etc/vars_pfx.conf"
ENV='/home/hoefkens/.wine'

env_paths={

'MET' : f'{ENV}/.meta',
'LDR' : f'{ENV}/.meta/loader',
'APP' : f'{ENV}/.meta/apps',
'ETC' : f'{ENV}/.meta/etc',
'ICO' : f'{ENV}/.meta/lib/ico',
'BIN' : f'{ENV}/.meta/bin',
'EXE' : f'{ENV}/.meta/exe',
		}

LDR=env_paths['LDR']
bin_wine={
		
'WINE'		:	f'{LDR}/bin/wine',
'WINE64'	:	f'{LDR}/bin/wine64',
'WINECFG'	:	f'{LDR}/bin/winecfg',
'WINEBOOT'	:	f'{LDR}/bin/wineboot',
'WINECMD'	:	f'{LDR}/bin/wineconsole',
'WINEMSI'	:	f'{LDR}/bin/msiexec',
'WINENPD'	:	f'{LDR}/bin/notepad',
		}

env_wine{


}

if __name__ == '__main__':
	main()
