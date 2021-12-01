#!/usr/bin/env python
from os import makedirs

def create_dtree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			makedirs(next_path)
			create_dtree(info, next_path)
	return