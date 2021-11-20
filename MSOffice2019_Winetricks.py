#!/usr/bin/env python
import os,sys
from subprocess import Popen,PIPE
from functools import partial
import conf

config=conf.glob
env = {
	**os.environ,
	'WINEDEBUG' 			: 	'-all',
	'WINEARCH'				:	'win64',
	'WINEDLLOVERRIDES'		:	'winemenubuilder.exe=d ',
	'WINEPREFIX' 			:	'/run/media/hoefkens/btrd0v1/opt/BTRWin/subv/MSOffice2019',
	'WINELOADER'			:	'/mnt/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wine64',
	'WINESERVER'			:	'/mnt/btrd0v1/opt/BTRWin/run/wine/lutris-6.14-4-x86_64/bin/wineserver'
}
sproc= partial( Popen, env=env, stdout=PIPE,
				universal_newlines=True,
				shell=True)
path={}
bin={}
path['mount']		= 	'/mnt/btrd0v1'
path['volume']		= 	'/opt/BTRWin/run'
path['runner']		= 	'/wine/lutris-6.14-4-x86_64/bin'
P=path
bin['winepath']		=	f"{P['mount']}{P['volume']}{P['runner']}/winepath"
bin['wine64']		=	f"{P['mount']}{P['volume']}{P['runner']}/wine"
bin['wineboot']		=	f"{P['mount']}{P['volume']}{P['runner']}/wineboot"
bin['wineserver']	=	f"{P['mount']}{P['volume']}{P['runner']}/wineserver"
bin['tricks']		=	f"/usr/bin/winetricks"
B=bin
args=sys.argv[1:]
strargs=''
for arg in args:
	strargs+= f'{arg} '
#sproc(f"{B['winepath']} -w {B['tricks']}")
#wineboot=subprocess.Popen(f"{B['wineboot']}",shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
#sproc(f"{B['wineserver']} -p 300 -d 1")
#print(f"{B['tricks']} {strargs}")
process=sproc(f"{B['tricks']} {strargs}")
while True:
	output = process.stdout.readline()
	d.print(output.strip())
	# Do something else
	return_code = process.poll()
	if return_code is not None:
		ret= return_code
		#wrl(f'RETURN CODE:{return_code}')
		# Process has finished, read rest of the output
		for output in process.stdout.readlines():
			d.print(output.strip())
		break
#os.system(f"env WINEPREFIX='/run/media/hoefkens/btrd0v1/opt/BTRWin/subv/MSOffice2019' {B['tricks']} {strargs}")

