#!/usr/bin/env python
import os
os.environ["BTRWIN_NAME"]='btrwin'
CFG									=	f'btrwin'
NAME								= f'{os.environ.get("BTRWIN_NAME")}'

DIR									=	{}
DIR["HOME"]					= f'{os.environ.get("HOME") if os.environ.get("HOME") else os.environ.get("HOMEPATH")}'
DIR["OS_CONFIG"]		=	f'/etc'
DIR["USER_CONFIG"]	= f'.config'

CONFIG							=	{}
CONFIG["OS"]				= F'{DIR["OS_CONFIG"]}'
CONFIG["SYS"]				=	f'{os.path.join(	DIR["OS_CONFIG"],	CFG													)}'
CONFIG["HOME"]			=	f'{os.path.join(	DIR["HOME"],			DIR["USER_CONFIG"]					)}'
CONFIG["USER"]			=	f'{os.path.join(	DIR["HOME"],			DIR["USER_CONFIG"],		NAME	)}'

USER_config					=	{}

# USER_config['DEFAULT']={
# 'ENV'			: '{os.environ}'
# 'ENVGET'	: '${ENV}.get'
# 'BTRNAME'	:	'${ENVGET}(BTRWIN_DEFAULT_NAME)
#
# [USER]
# NAME: ${ENV}['USER']
# HOME: ${ENV}['HOME']
# CONFDIR:	${HOME}/.config
#
#
# [CONFIG]
# OS:
# SYS:
# HOME:{}