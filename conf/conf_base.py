#!/usr/bin/env python
CONF={}

def init():
	global CONF
	CONF['SYS'] = '/etc/betterwin/sys.conf'



def main():
	global testvar
	testvar = "var imported"
	print(testvar)




if __name__ == '__main__':
	main()
	
if __name__ != '__main__':
	init()