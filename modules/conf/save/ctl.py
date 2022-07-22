#!/usr/bin/env python
#	STRUCT	::PROJECT:;PKG:;MOD:;TYPE:;PATH:..
#	META	::AUTHOR:;PIM:;PATH:hoefkensj.github.io
#	LEGAL	::LICENSE:
import os
import btrwin.lib.conf

def save_global_config(G):

	for configfile in G.keys():
		if configfile == 'btrwin':
			path='/etc/btrwin/btrwin.conf'
		else:
			path=os.path.join(os.getenv("HOME"), '.config/btrwin', f'{configfile}.conf')
		config=G[configfile]
		btrwin.lib.conf.savefile(path, config)