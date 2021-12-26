#!/usr/bin/env python
import btrwin.ui.cli.cli as cli
entrypoint= cli.entry_point

def main():
	entrypoint(prog_name='Btrwin')
	
if __name__ == '__main__':
	main()
