#!/usr/bin/env python
import betterwin
import fnx.conf.load.ctl
G= fnx.conf.load.main.global_config()

def read_skell(skel):
	with open(skel) as template:
		tpl= template.readlines()
	
	def head(tpl):
		for idx,line in enumerate(tpl):
			if 'cfg_start' in line:
				header=tpl[0:idx]
				return header
	def bottom(tpl):			
		for idx,line in enumerate(tpl):				
			if 'cfg_stop' in line:
				bottom=tpl[idx:]
				return bottom
				
	return [[head(tpl)],[bottom(tpl)]]
	
def create_binpy():
	pass
	
def winebin():
	bins=['msiexec','notepad','regedit','regsvr32','wine','wine64','wineboot','winecfg','wineconsole','winepath','wineserver']
	for bin in bins:
		yield bin
	print((next(bins))
	
def main(pfx):
	PFX=pfx
	EXEC=''
	print(next(winebin()))
	print(next(winebin()))

if __name__ == '__main__':
