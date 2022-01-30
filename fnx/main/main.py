#!/usr/bin/env python
import btrwin.interface.ui.cli_ctl.main as cli
entrypoint= cli.entry_point

def main():
	entrypoint(prog_name='Btrwin')
	
if __name__ == '__main__':
	main()
