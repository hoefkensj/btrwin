#!/usr/bin/env python

from btrwin import G
G=G()

init={}


init['	'sys':'${mount}/opt/btrwin',
init['	'subv' : '${sys}/subv',
init['	'loaders' : '${sys}/loaders'
							'file': file,
							'section': section,
#1: choose  install name [default = btrwin] (if you already have a system on one btrfs volume ... )
init['config']= f'/etc/btrwin/{name}.conf'

#2 choose te btrfs volume
init['btrfsvol'