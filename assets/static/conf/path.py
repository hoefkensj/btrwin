#!/usr/bin/env python
import os
os.environ["BTRWIN_WORLD"]='btrwin'
CFG									=	f'btrwin'
WORLD								= f'{os.environ.get("BTRWIN_WORLD")}'

DIR									=	{}
DIR["HOME"]					= f'{os.environ.get("HOME") if os.environ.get("HOME") else os.environ.get("HOMEPATH")}'
DIR['OS_ROOT']			= f'{os.path.join(DIR["HOME"], "BTRWIN_FAKEROOT")}'
#DIR['OS_ROOT']			= f'/'
DIR["OS_CONFIG"]		=	f'etc'
DIR["USER_CONFIG"]	= f'.config'

CONFIG							=	{}
CONFIG["OS"]				= F'{os.path.join(	DIR["OS_ROOT"],		DIR["OS_CONFIG"]						)}'
CONFIG["SYS"]				=	f'{os.path.join(	DIR["OS_ROOT"],		DIR["OS_CONFIG"],	CFG				)}'
CONFIG["HOME"]			=	f'{os.path.join(	DIR["HOME"],			DIR["USER_CONFIG"]					)}'
CONFIG["USER"]			=	f'{os.path.join(	DIR["HOME"],			DIR["USER_CONFIG"],		WORLD	)}'

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