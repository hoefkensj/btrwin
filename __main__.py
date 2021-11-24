#!/usr/bin/env python3
"""Example MILC program that shows off many features.

PYTHON_ARGCOMPLETE_OK
"""

from milc import cli
from betterwin import fsctl,pfx,common,exec,loader,skel,tpl


@cli.entrypoint('betterwin')
def main(cli):
    cli.log.info('No subcommand specified!')
    cli.print_usage()


@cli.subcommand('fsctl')
def fsctl(cli):
    cli.echo('{fg_green}Hello, %s!', cli.config.general.name)
    















if __name__ == '__main__':
    cli()
	#!/usr/bin/env python
