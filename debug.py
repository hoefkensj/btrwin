#!/usr/bin/env python
from sys import stdout
import os

def print(*a):
	for item in a :
		stdout.write(str(item))
	#stdout.write(f'\n')
	return
	

