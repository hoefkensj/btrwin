import os,ast
import confctl
conf_pfx=confctl.glob['Office']
e= '''{
'WINEDEBUG' 			: 	f"{conf_pfx['WINE_ENV']['WINEDEBUG']}",
'WINEARCH'				:	f"{conf_pfx['WINE_ENV']['WINEARCH']}",
'WINEDLLOVERRIDES'		:	f"{conf_pfx['WINE_ENV']['WINEDLLOVERRIDES']}",
'WINEPREFIX' 			:	f"{conf_pfx['WINE_ENV']['WINEPREFIX']}",
'WINELOADER'			:	f"{conf_pfx['WINE_ENV']['WINELOADER']}",
'WINESERVER'			:	f"{conf_pfx['WINE_ENV']['WINESERVER']}"}'''

b=ast.literal_eval('''{
'WINEDEBUG' 			: 	f"{conf_pfx['WINE_ENV']['WINEDEBUG']}",
'WINEARCH'				:	f"{conf_pfx['WINE_ENV']['WINEARCH']}",
'WINEDLLOVERRIDES'		:	f"{conf_pfx['WINE_ENV']['WINEDLLOVERRIDES']}",
'WINEPREFIX' 			:	f"{conf_pfx['WINE_ENV']['WINEPREFIX']}",
'WINELOADER'			:	f"{conf_pfx['WINE_ENV']['WINELOADER']}",
'WINESERVER'			:	f"{conf_pfx['WINE_ENV']['WINESERVER']}"}''')
print(b)

