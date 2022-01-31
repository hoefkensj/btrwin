#!/usr/bin/env python
from lib.fs import ls_blkpart

found= ls_blkpart(FSTYPE='btrfs')
print(found)
		
