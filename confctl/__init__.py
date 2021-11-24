#!/usr/bin/env python
from betterwin.confctl import confctl

glob=confctl.get_global_config()

if __name__ == '__main__':
	print(glob)