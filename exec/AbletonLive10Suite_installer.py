#!/usr/bin/env python
import os
from subprocess import Popen,PIPE
from functools import partial
import confctl

config=confctl.glob

env = {
	**os.environ,
	'WINEDEBUG' 			: 	'all',
	'WINEARCH'				:	'win64',
	'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
	'WINEPREFIX' 			:	'/mnt/btrd0v1/opt/BTRWin/subv/win10',
	'WINELOADER'			:	'/mnt/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wine',
	'WINESERVER'			:	'/mnt/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wineserver'
}
sproc= partial( Popen, env=env, stdout=PIPE,
				universal_newlines=True,
				shell=True)
path={}
bin={}
path['mount']		= 	'/run/media/hoefkens/btrd0v1'
path['volume']		= 	'/opt/BTRWin/run'
path['runner']		= 	'/wine/lutris-6.14-4-x86_64/bin'
P=path
bin['winepath']		=	f"{P['mount']}{P['volume']}{P['runner']}/winepath"
bin['wine64']		=	f"{P['mount']}{P['volume']}{P['runner']}/wine64"
bin['wineboot']		=	f"{P['mount']}{P['volume']}{P['runner']}/wineboot"
bin['wineserver']	=	f"{P['mount']}{P['volume']}{P['runner']}/wineserver"
bin['exec']		=	'/run/media/hoefkens/DATA/Live10Thinapp/AbletonLive10Suite.msi' #winepath.stdout.readline()
B=bin
sproc(f"{B['winepath']} -w {B['exec']}")
#wineboot=subprocess.Popen(f"{B['wineboot']}",shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
#sproc(f"{B['wineserver']} -p 300 -d2")
sproc(f"{B['wine64']} msiexec /i {B['exec']}")

