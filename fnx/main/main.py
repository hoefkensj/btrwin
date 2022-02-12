#!/usr/bin/env python
import interface.ui.cli.ctl.main as cli
entrypoint= cli.entry_point

def main():
	entrypoint(prog_name='Btrwin')
	
if __name__ == '__main__':
	main()
