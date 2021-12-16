#!/usr/bin/env python
from .ctl import get_global_config
from .ctl import show_global_config
from .ctl import save_global_config
from .ctl import create_new_sysconf

def get():
	return get_global_config()

def save(G):
	save_global_config(G)

def show():
	show_global_config()


	
