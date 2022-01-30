#!/usr/bin/env python
import os,subprocess
from fnx.conf import ctl


PFX			=	'Win10'
bin=['winepath','wine64','wine','wineboot','winecfg','wineconsole','notepad','msiexec','wineserver','regsvr32','regedit',]
env=['WINEDEBUG','WINEARCH','WINEDLLOVERRIDES','WINEPREFIX','WINELOADER','WINESERVER']
WINE_ENV= ctl.confctl.glob[PFX]['WINE_ENV']
WINE_BIN= ctl.confctl.glob[PFX]['WINE_BIN']

b={key : WINE_BIN[key.upper()] for key in bin}
e={**os.environ,**{key: WINE_ENV[key] for key in env}}
#print(f"{'EXE' if __file__.split('/')[-1:][0].split('_')[-1:][0].split('.')[-1].isupper() else 'exe'}")

b['exec']	=	f"{ctl.confctl.glob[PFX]['PATH']['path']}/drive_c/FooDAW2000/FooDAW2000/foobar2000/foobar2000.exe"
winepath	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)
sproc		=	subprocess.Popen(f"{b['wine']} {str(winepath.strip())[2:-1]}" ,env=e,shell=True)


