#!/usr/bin/env python

import __main__
import confctl
global glob_config
glob_config = confctl.from_globconf()
print('test')