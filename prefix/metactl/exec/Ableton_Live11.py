
#!/usr/bin/env python
import os,subprocess
import conf,assets
	
PFX			=	'Ableton'
	
conf_pfx	= 	conf.glob[PFX]
env			=	assets.env
b			=	assets.b
b['exec']	=	f"{conf_pfx['PATH']['exes']}/live.exe"
winepath	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)
sproc		=	subprocess.Popen(f"{b['wine']} {str(winepath.strip())[2:-1]}" ,env=env,shell=True)
