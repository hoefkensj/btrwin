#!/usr/bin/env python
import requests
import sys
sprint=sys.stdout.write

lutris_api='https://lutris.net/api/runners?format=json&search=wine'
def lutris():
	responce= requests.get(lutris_api)
	print(responce.json())

	# dicts=sepdict(responce.text)
	# for dct in dicts:
	# 	for keyval in dct.split(','):
	# 		nested=sepdict(keyval)
	# 		for nest in nested:
	# 			print(nest)


def sepdict(string,open=[] ,all=[]):
	contents=''
	for idx,char in enumerate(string):
		if char == '{':
			open+=[idx+1]
		elif char=='}':
			last=string[open[-1]:idx]
			open=open[0:-1]
			all+=[last]

	return all
lutris()