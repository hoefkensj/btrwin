#!/usr/bin/env python
import debug as d
from . import confctl as main
from . import conf_base as BASE

#global glob_config
d.print('glob from globconf')
glob = main.from_globconf()
