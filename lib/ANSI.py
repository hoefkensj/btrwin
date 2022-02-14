#!/usr/bin/env python
import sys
import types

def ANSI_fn(fn):
	def ansi(SEQ):
		def ANSIseq(ESC='\033', SEQ='{SEQ}', FN='{FN}'):
			return '{ESC}[{SEQ}{FN}'.format(ESC=ESC,SEQ=SEQ,FN=FN)
		return ANSIseq(SEQ=SEQ,FN=fn)
	return ansi
	
	ANSI_E= ANSI_fn('E')
	ANSI_F= ANSI_fn('F')
	ANSI_G= ANSI_fn('G')
	ANSI_H= ANSI_fn('H')
	ANSI_K= ANSI_fn('K')
	ANSI_m= ANSI_fn('m')

def m(**k):
	ANSI_m= ANSI_fn('m')
	if k.get('style'):
		styles={
						'reset' 	:	 ANSI_m(0),
						'bold' 		:	 ANSI_m(1),
						'ital' 		:	 ANSI_m(2),
						'line' 		:	 ANSI_m(4),
						'blink' 	:	 ANSI_m(5),
						'inv' 		:	 ANSI_m(7),
						'strike' 	:	 ANSI_m(9),
						'noblink' :	 ANSI_m(25),
						'gray' 		:	 ANSI_m(30),
						'red' 		:	 ANSI_m(31),
						'green' 	:	 ANSI_m(32),
						'yellow' 	:	 ANSI_m(33),
						'blue' 		:	 ANSI_m(34),
						'purple' 	:	 ANSI_m(35),
						'bluegreen' 	:	 ANSI_m(36),
						'white' 	:	 ANSI_m(37),
		}
		return styles[k.get('style')]
		
	ANSIm=types.SimpleNamespace()
	ANSIm.reset		=	ANSI_m(0)
	ANSIm.bold		=	ANSI_m(1)
	ANSIm.ital		=	ANSI_m(2)
	ANSIm.line		=	ANSI_m(4)
	ANSIm.blink		=	ANSI_m(5)
	ANSIm.inv			=	ANSI_m(7)
	ANSIm.strike	=	ANSI_m(9)
	ANSIm.noblink	=	ANSI_m(25)
	ANSIm.gray		=	ANSI_m(30)
	ANSIm.red			=	ANSI_m(31)
	ANSIm.green		=	ANSI_m(32)
	ANSIm.yellow	=	ANSI_m(33)
	ANSIm.blue		=	ANSI_m(34)
	ANSIm.purple	=	ANSI_m(35)
	ANSIm.bluegreen	=	ANSI_m(36)
	ANSIm.white		=	ANSI_m(37)
	return ANSIm
m=m()

def txt(**k):
	markup=[m(style=style) for style in k.get('m') if k.get('m')]
	reset=m(style='reset') if k.get('text')[-7:] != m(style='reset') else ''
	return '{markup}{text}{reset}'.format(markup=str().join(markup),text=k.get('text'),reset=str().join(reset))

def settxt(*a, **k):
	text= k.get('txt') if k.get('txt') else str().join(a) if a else ''
	styles=[style for style in k.get('style') if k.get('style')]
	txt_styled=txt(text=text, m=styles)
	def stdout_text():
		return str(txt_styled)
	return stdout_text()

def setstyle(**k):
	text='{placeholder}'
	styles=[style for style in k.get('style') if k.get('style')]
	txt_styled=txt(text=text, m=styles)
	def stdout_text(text):
		return str(txt_styled.format(placeholder=text))
	return stdout_text

def styled(*a, **k):
 return txt(text=k.get('txt') or a[0], m=k.get('style'))

def table(**k):
	pass

def stdout_write(*a,**k):
	def write(*a,**k):
		sys.stdout.write(styled(*a, **k))
		sys.stdout.write(m('reset'))
		sys.stdout.flush()
	return write

style_green=setstyle(style=['green'])
style_blue=setstyle(style=['blue'])
style_blue=setstyle(style=['red'])
style_bold=setstyle(style=['bold'])
style_line=setstyle(style=['line'])
style_blink=setstyle(style=['blink'])

def load_presets():
	mem= types.SimpleNamespace()

	# txt_test\
	mem.DONE=style_green('DONE')
	mem.MARK=style_green('*')
	mem.BUSY=style_blink(style_green('BUSY'))
	mem.CHECK=style_bold('Checking :')
	mem.PROC=style_bold('Processing :')
	# stdout_write(txt='test', style=['red','line'], org='tit2')
	return mem