#!/usr/bin/env python
import os,subprocess

bin_winepath='/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/winepath'
bin_wine64='/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wine64'
bin_wineboot='/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wineboot'
bin_winword='/run/media/hoefkens/btrd0v1/opt/BTRWin/subv/Win10/drive_c/Start/OInstall.exe'
bin_wineserver='/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wineserver'
env = {
	**os.environ,
	'WINEDEBUG' 			: 	'-all',
	'WINEARCH'				:	'win64',
	'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
	'WINEPREFIX' 			:	'/run/media/hoefkens/btrd0v1/opt/BTRWin/subv/MSOffice2019/',
	'WINELOADER'			:	'/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wine',
	'WINESERVER'			:	'/run/media/hoefkens/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wineserver'
}
winepath=subprocess.Popen(f'{bin_winepath} -w {bin_winword}',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
wordpath=winepath.stdout.readline()
#wineboot=subprocess.Popen(f'{bin_wineboot}',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
winserver=subprocess.Popen(f'{bin_wineserver} -p 300 -d2',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
runwin64=subprocess.Popen(f'{bin_wine64} {bin_winword}',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)

