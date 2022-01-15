#!/usr/bin/env python
import os
import btrwin.lib as lib
import btrwin.units as units
# copy wines
#delete orig folder
#make link original location nto central

def detect_wine(parentdir):
		candidates = lib.fs.ls_dirs(parentdir)
		for d in candidates:
			print(d)

dirs= [units.setup.runner_paths.wine_locs[k].format(USERHOME=os.environ.get('HOME')) for k in units.setup.runner_paths.wine_locs.keys()]

for d in dirs:
	try:
		detect_wine(d.format(USERHOME=os.environ.get('HOME')))
	except FileNotFoundError:
		print('no dir here')