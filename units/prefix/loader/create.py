#!/usr/bin/env python
import argparse



def content(PFX='',EXE=''):


	content_a = '''
#!/usr/bin/env python
import os,subprocess
import conf,common
	'''
	content_b=f'''
PFX			=	'{PFX}'
	'''
	content_c= '''
conf_pfx	= 	conf.glob[PFX]
env			=	common.env
b			=	common.b
'''
	content_d = "b['exec']	=	"+	'f"{conf_pfx['+"'PATH']['exes']}/"+EXE+'"'
	content_e='''
winepath	=	subprocess.check_output(f"{b['winepath']} -w {b['exec']}", shell=True)
sproc		=	subprocess.Popen(f"{b['wine']} {str(winepath.strip())[2:-1]}" ,env=env,shell=True)
'''
	content=f'{content_a}{content_b}{content_c}{content_d}{content_e}'
	print(content)
	return content

def write_file(filename,PFX='',EXE=''):
	with open(filename, 'w') as file:
		file.write(content(PFX,EXE))

if __name__=='__main__':
	write_file('MSOffice2010_WINWORD.py',PFX='Ableton',EXE='WINWORD.EXE')