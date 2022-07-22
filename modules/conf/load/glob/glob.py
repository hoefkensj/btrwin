#!/usr/bin/env python
import btrwin.lib.conf

def rc(**k):
	G=k.get('G') or btrwin.lib.conf.new()
	btrwin.lib.conf.new()