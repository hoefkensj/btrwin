#!/usr/bin/env python
import btrwin.units as units

# there is no combination i see where all 3 work how id prefer one of the last 2 since i can make all imports relative to the 'master' package and not to its own location
# how do i get pycharm to see that module as the parent module its already marked as a source folder and as a project folder ...

def main():
	units.ui.cli.cli.entry_point()


if __name__ == '__main__':
	main()
