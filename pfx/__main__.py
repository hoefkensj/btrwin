#!/usr/bin/env python

from milc import cli

from betterwin.pfx import scan




#@cli.entrypoint('main')
@cli.entrypoint('')
def main(cli):
	cli.print_usage()

@cli.argument('tpl', help='template to use as src',default='tpl-Win64_20211121v1' )
@cli.argument('name', help='new prefix name')
@cli.subcommand('create')
def create(cli):
	pfx.new.create_new_prefix(cli.config.create.name,cli.config.create.tpl)

@cli.argument('ext',choices=['exe','lnk'], help='scan for exe or lnk' )
@cli.argument('prefix', help='prefix to scan name')
@cli.subcommand('scan')
def scann(cli):
	scan.scn_ext(cli.config.scan.prefix,cli.config.scan.ext,data=[])











if __name__ == '__main__':
    cli()