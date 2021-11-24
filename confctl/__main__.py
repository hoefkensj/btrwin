#!/usr/bin/env python
from betterwin.confctl import confctl

glob=confctl.get_global_config()

if __name__ == '__main__':
	[print(glob['betterwin'][section]) for section in  glob['betterwin']]
	[print(key) for key in  glob['betterwin']['PATH']]