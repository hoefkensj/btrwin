#!/usr/bin/env python
import argparse
import debug as d

def parseArgs():
	parser = argparse.ArgumentParser(prog='loaderctl',description='win(wine|winex|xover|proton) loader control')
	parser.add_argument('-l','--loader', choices=['wine', 'proton'], type=str,  help='')#nargs="+"
	
	parser.add_argument('-e','--edition', choices=['wine', 'xover', 'proton'], type=str,  help='')
	parser.add_argument('-v','--verbose', action='store_true', help='Show the list of recorded readings of the current test')
	parser.add_argument('-s','--stress', action='store_true', help='Apply stress test to the CPU while the test is running')
	args = parser.parse_args()
	return args

def ldr_wine():
	d.print(ldr_wine)
	
def ldr_proton():
	d.print(ldr_proton)



def main():
	args=parseArgs()
	case = {
		'wine' : ldr_wine,
		'proton' : ldr_proton
	}
	print(args.loader)


if __name__ == '__main__':
	main()
