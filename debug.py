#!/usr/bin/env python
from sys import stdout


def print(*a):
	for item in a :
		stdout.write(f'{item} ')
	stdout.write(f'\n')
	return
	
	

