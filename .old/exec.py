#!/usr/bin/env python
import os
e= '''{
		**os.environ,
		'WINEDEBUG' 			: 	f"{conf_pfx['WINE_ENV']['WINEDEBUG']}",
		'WINEARCH'				:	f"{conf_pfx['WINE_ENV']['WINEARCH']}",
		'WINEDLLOVERRIDES'		:	f"{conf_pfx['WINE_ENV']['WINEDLLOVERRIDES']}",
		'WINEPREFIX' 			:	f"{conf_pfx['WINE_ENV']['WINEPREFIX']}",
		'WINELOADER'			:	f"{conf_pfx['WINE_ENV']['WINELOADER']}",
		'WINESERVER'			:	f"{conf_pfx['WINE_ENV']['WINESERVER']}",}'''
		
b={
		# 'winepath'				:	f"{conf_pfx['WINE_BIN']['WINEPATH']}",
		# 'wine64'				:	f"{conf_pfx['WINE_BIN']['WINE64']}",
		# 'wine'					:	f"{conf_pfx['WINE_BIN']['WINE']}",
		# 'wineboot'				:	f"{conf_pfx['WINE_BIN']['WINEBOOT']}",
		# 'winecfg'				:	f"{conf_pfx['WINE_BIN']['WINECFG']}",
		# 'wineconsole'			:	f"{conf_pfx['WINE_BIN']['WINECONSOLE']}",
		# 'notepad'				:	f"{conf_pfx['WINE_BIN']['WINENOTEPAD']}",
		# 'msiexec'				:	f"{conf_pfx['WINE_BIN']['WINEMSIEXEC']}",
		# 'wineserver'			:	f"{conf_pfx['WINE_BIN']['WINESERVER']}",
		# 'regsvr32'				:	f"{conf_pfx['WINE_BIN']['WINEREGSVR']}",
		# 'regedit'				:	f"{conf_pfx['WINE_BIN']['WINEREGEDIT']}",
	}
	





