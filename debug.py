#!/usr/bin/env python
from sys import stdout
import os

def print(*a):
	prnt=''
	for item in a :
		prnt+=str(item)
	prnt+= '\n'
	stdout.write(prnt)
	#stdout.write(f'\n')
	return
	

