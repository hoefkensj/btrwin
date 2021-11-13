#!/usr/bin/env python
import  conf
import btrfs
from functools import partial

import test


#creating the btrfs subvol

def f_create_template(name,glob_config):
	globcfg_subv=glob_config['SYS']['PATH']['subv']
	list=get_subvs()
	print(list)
	create_subv('/mnt/btrd0v1/opt/BTRWin/subv', 'tpl-w1064_20211112v1')
	list=get_subvs('/mnt/btrd0v1/opt/BTRWin/subv')
	print(list)

	# create_template=partial(f_create_template ,glob_config=
	
	


def main():
	pass


if __name__ == '__main__':
	main()
