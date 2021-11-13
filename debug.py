#!/usr/bin/env python
import conf
conf.glob_config['dev']= { 'debug'  : 1}

def print(*a):
	if conf.glob_config['dev']['debug']==1 :
		print(a)
	
	

def main():
	print('main ran')


if __name__ == '__main__':
	main()
