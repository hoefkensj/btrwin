def s_default(name,PATH):
	default={'file' 	:		name,
		'sectio'	:		'DEFAULT',
		'NAME'		:		f'{name}',
		'PATH'		:		f'{PATH}',
		'SYS'			:		f'{PATH}/{name}',
		'LDRS'		:		f'{PATH}/{name}/loaders/',
		'WLDRS'		:		f'{PATH}/{name}/loaders/wine/',
	}
	return default
	
def s_dirs(name):
	dirs={
		'file' 			:		name,
		'section'		:		'DIRS',
		'btrwin'		:		'${SYS}',
		'bin'				:		'${SYS}/bin',
		'apps'			:		'${SYS}/apps',
		'subv'			:		'${SYS}/subv',
		'loaders'		:		'${SYS}/loaders',
		'proton'		:		'${LDRS}/proton',
		'wine'			:		'${LDRS}/wine',
		'crossover'	:		'${LDRS}/crossover',
		'default'		:		'${SYS}/default',
	}
	return dirs

def s_init(name,mount,pth):
	sys=os.path.join('${mout}', pth,'btrwin')
	init={
		'file' 			:		name,
		'section'		:		'PATH',
		'config'		:		f'/etc/btrwin/{name}.conf',
		'mount'			:		mount,
		'sys'				:		sys ,
		'loaders'		:		'${SYS}/loaders',
		'subv'			:		'${SYS}subv',
	}
	return init



# def s_tluafed(name, PATH):
# 	tluafed= {
# 		'file' 		:		name,
# 		'section'	:		'TLUAFED',
# 		'NAME'		:		f'{name}',
# 		'PATH'		:		f'{PATH}',
# 		'SYS'			:		f'{PATH}/{name}',
# 		'LDRS'		:		f'{PATH}/{name}/loaders/',
# 		'WLDRS'		:		f'{PATH}/{name}/loaders/wine/',
# 		}
# 	G=units.conf.load()
# 	lib.conf.set_dict(tluafed, G)
# 	units.conf.save(G)
# 	return units.conf.load()
