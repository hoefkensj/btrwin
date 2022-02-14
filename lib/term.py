#!/usr/bin/env python
import re
import shutil
import sys
import termios
import tty

def term_init():
	try:
		termwidth=shutil.get_terminal_size()[0]
	except Exception as E:
		print(E)

def term_cursorloc():
	buf = ""
	stdin = sys.stdin.fileno()
	tattr = termios.tcgetattr(stdin)
	try:
		tty.setcbreak(stdin, termios.TCSANOW)
		sys.stdout.write("\x1b[6n")
		sys.stdout.flush()
		while True:
			buf += sys.stdin.read(1)
			if buf[-1] == "R":
				break
	finally:
		termios.tcsetattr(stdin, termios.TCSANOW, tattr)
	# reading the actual values, but what if a keystroke appears while reading
	# from stdin? As dirty work around, getpos() returns if this fails: None
	try:
		matches = re.match(r"^\x1b\[(\d*);(\d*)R", buf)
		groups = matches.groups()
	except AttributeError:
		return None
	return (int(groups[0]), int(groups[1]))

def TERM_init(**k):
	def init_term():
		try:
			termwidth=shutil.get_terminal_size()[0]
			termheight=shutil.get_terminal_size()[1]
		except Exception as E:
			print(E)
		finally:
			return termwidth,termheight
	def update_term():
			return shutil.get_terminal_size()[0],shutil.get_terminal_size()[1]
	
	def cursor():
		return term_cursorloc()
	
	start= cursor()
	h,w=init_term()
	return [(h,w),start]