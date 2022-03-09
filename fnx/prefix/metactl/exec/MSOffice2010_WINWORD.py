#!/usr/bin/env python
import os,subprocess

env = {
	**os.environ,
	'WINEDEBUG' 			: 	'-all',
	'WINEARCH'				:	'win64',
	'WINEPREFIX' 			:	'/home/hoefkens/Games/Heroic/Prefixes/Red-Dead-Redemption-2/',
	'WINELOADER'			:	'/opt/btrwin/loaders/wine/lutris-6.21-6-x86_64/bin/wine64',
	'WINESERVER'			:	'/opt/btrwin/loaders/wine/lutris-6.21-6-x86_64/bin/wineserver',
	'FONTCONFIG_FILE' : "/home/hoefkens/.wine/myfonts/fonts.conf",
	'FONTCONFIG_PATH' : "/home/hoefkens/wine/myfonts"
}


bin=['winepath','wine64','wine','wineboot','winecfg','wineconsole','notepad','msiexec','wineserver','regsvr32','regedit',]

b={key : f'/opt/btrwin/loaders/wine/lutris-6.21-6-x86_64/bin/{key}' for key in bin}


#print(f"{'EXE' if __file__.split('/')[-1:][0].split('_')[-1:][0].split('.')[-1].isupper() else 'exe'}")
b['exec']	=	f"/run/media/hoefkens/btrsdv1/Games/Epic/RedDeadRedemption2/PlayRDR2.exe"

winepath2	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)

winserver=subprocess.Popen(f"{b['wineserver']} -p 300 -d0",shell=True,env=env,stdout=subprocess.PIPE)
sproc		=	subprocess.Popen(f"{b['wine64']} {str(winepath2.strip())[2:-2]}" ,env=env,shell=True)


