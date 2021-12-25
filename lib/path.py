#!/usr/bin/env python
import os
os.environ["BTRWIN_NAME"]='btrwin'

CONFIG							= {}
DIR									=	{}
CFG									=	f'btrwin'
NAME								= f'{os.environ.get("BTRWIN_NAME")}'
DIR["HOME"]					= f'{os.environ.get("HOME")}'
CONFIG["OS"]				= f'/etc'
CONFIG["SYS"]				= f'{CONFIG["OS"]}/{CFG}'
CONFIG["HOME"]			=	f'{DIR["HOME"]}/.config'
CONFIG["USER"]			= f'{CONFIG["HOME"]}/{NAME}'