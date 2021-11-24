#!/usr/bin/env python

def get_dirs(parent):
	return [os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]

