#!/usr/bin/env python
def getargs(): #get arguments from commandline
	parser=argparse.ArgumentParser()
	parser.add_argument('PREFIX', help='name of the prefix')
	parser.add_argument('BIT', type=str ,help='WINE ARCH')
	parser.add_argument('--EXES', type=str ,help='space " "-less folder With EXES')
	args = parser.parse_args()
	return args