#!/usr/bin/env python
import os,subprocess
import conf
from conf import ctl


PFX			=	'Office'
bin=['winepath','wine64','wine','wineboot','winecfg','wineconsole','notepad','msiexec','wineserver','regsvr32','regedit',]
env=['WINEDEBUG','WINEARCH','WINEDLLOVERRIDES','WINEPREFIX','WINELOADER','WINESERVER']
WINE_ENV=ctl.glob[PFX]['WINE_ENV']
WINE_BIN=ctl.glob[PFX]['WINE_BIN']

b={key : WINE_BIN[key.upper()] for key in bin}
e={**os.environ,**{key: WINE_ENV[key] for key in env}}
#print(f"{'EXE' if __file__.split('/')[-1:][0].split('_')[-1:][0].split('.')[-1].isupper() else 'exe'}")

b['exec']	=	f"{ctl.glob[PFX]['PATH']['exes']}/{__file__.split('/')[-1:][0].split('_')[-1:][0].split('.')[0]}.EXE"
winepath	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)
sproc		=	subprocess.Popen(f"{b['wine']} {str(winepath.strip())[2:-1]}" ,env=e,shell=True)


