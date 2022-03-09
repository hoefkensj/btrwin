#!/usr/bin/env python
import os
import subprocess





'''/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wine64 \''''
'''/opt/Adobe/PhotoshopCC/prefix/drive_c/users/hoefkens/PhotoshopSE/Photoshop.exe'''

env={
**os.environ,
'WINEDEBUG' 			: '-all',
'WINEARCH'				:	'win64',
'WINEPREFIX' 			:	'/opt/Adobe/PhotoshopCC/prefix',
'WINELOADER'			:	'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wine',
'WINESERVER'			:	'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wineserver',
'FONTCONFIG_FILE' : '/opt/btrwin/lib/fonts/fonts/fonts.conf',
'FONTCONFIG_PATH' : '/opt/btrwin/lib/fonts/fonts/',
'SCR_PATH'				:	'/opt/Adobe/PhotoshopCC',
'RESOURCES_PATH'	:	'/opt/Adobe/PhotoshopCC/resources',
'CACHE_PATH'			: '/home/hoefkens/.cache/photoshopCCV19'
}


winepath=subprocess.run(f'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/winepath -w /opt/Adobe/PhotoshopCC/prefix/drive_c/users/hoefkens/PhotoshopSE/Photoshop.exe',
															shell=True,
															env=env,
															universal_newlines=True,
															capture_output=True).stdout

#wineboot=subprocess.Popen(f'{bin_wineboot}',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
#winserver=subprocess.Popen(f'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wineserver -p -d2',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)
runwin64=subprocess.Popen(f'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wine64 /opt/Adobe/PhotoshopCC/prefix/drive_c/users/hoefkens/PhotoshopSE/Photoshop.exe',shell=True,env=env,stdout=subprocess.PIPE,universal_newlines=True)