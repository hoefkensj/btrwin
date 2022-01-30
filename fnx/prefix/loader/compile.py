#!/usr/bin/env python
import subprocess,argparse

def getargs(): #get arguments from commandline
	parser=argparse.ArgumentParser()
	parser.add_argument('-i','--follow-imports',action='store_true' ,help='--follow imports')
	parser.add_argument('-1', '--onefile', action='store_true' ,help='--onefile')
	parser.add_argument('script', help='script.py|SCRIPT.PY')
	args = parser.parse_args()
	return args

# MSOffice2010_EXCEL.PY'

def main():
	a=getargs()
	cmd=f'python -m nuitka {"--follow-imports" if a.follow_imports else ""} {"--onefile" if a.onefile else ""}{a.script}'# --follow-imports
	proc=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,universal_newlines=True)
	while True:
		print(proc.stdout.readline().strip())
		if proc.poll() is not None:
			print(proc.stdout.readlines())
			break
	print(a)

if __name__ == '__main__':
	getargs()
	main()
