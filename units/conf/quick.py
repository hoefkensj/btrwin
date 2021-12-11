#!/usr/bin/env python
from btrwin.units.conf import ctl




def get():
	return ctl.get_global_config()
	
def save(G):
	ctl.save_global_config(G)

def set(key,value,section,file):
	ctl.set_key(file=file,section=section,key=key,value=value)
	
def show():
	ctl.show_global_config()

