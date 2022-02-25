#!/usr/bin/env python
import sys
import types


def fn(fn):
	def ansi(SEQ):
		def ANSIseq(ESC='\033', SEQ='{SEQ}', FN='{FN}'):
			return '{ESC}[{SEQ}{FN}'.format(ESC=ESC,SEQ=SEQ,FN=FN)
		return ANSIseq(SEQ=SEQ,FN=fn)
	return ansi

def ANSI():
	ANSI=types.SimpleNamespace()	
	ANSI.E	= fn('E')
	ANSI.F	= fn('F')
	ANSI.G	= fn('G')
	ANSI.H	= fn('H')
	ANSI.K	= fn('K')
	ANSI.m	= fn('m')
	return ANSI
ANSI=ANSI()

def ANSIm():		
	m=types.SimpleNamespace()
	m.reset		=	ANSI.m(0)
	m.bold		=	ANSI.m(1)
	m.ital		=	ANSI.m(2)
	m.line		=	ANSI.m(4)
	m.blink		=	ANSI.m(5)
	m.inv			=	ANSI.m(7)
	m.strike	=	ANSI.m(9)
	m.noblink	=	ANSI.m(25)
	m.gray		=	ANSI.m(30)
	m.red			=	ANSI.m(31)
	m.green		=	ANSI.m(32)
	m.yellow	=	ANSI.m(33)
	m.blue		=	ANSI.m(34)
	m.purple	=	ANSI.m(35)
	m.bluegreen	=	ANSI.m(36)
	m.white		=	ANSI.m(37)
	return m
ANSI.m=ANSIm()

ANSI_E= fn('E')
ANSI_F= fn('F')
ANSI_G= fn('G')
ANSI_H= fn('H')
ANSI_K= fn('K')
ANSI_m= fn('m')

def markup(a):
	styles={
		'reset' 	:	 ANSI.m.reset,
		'bold' 		:	 ANSI.m.bold,
		'ital' 		:	 ANSI.m.ital,
		'line' 		:	 ANSI.m.line,
		'blink' 	:	 ANSI.m.blink,
		'inv' 		:	 ANSI.m.inv,
		'strike' 	:	 ANSI.m.strike,
		'noblink' :	 ANSI.m.noblink,
		'gray' 		:	 ANSI.m.gray,
		'red' 		:	 ANSI.m.red,
		'green' 	:	 ANSI.m.green,
		'yellow' 	:	 ANSI.m.yellow,
		'blue' 		:	 ANSI.m.blue,
		'purple' 	:	 ANSI.m.purple,
		'blgreen' :	 ANSI.m.bluegreen,
		'white' 	:	 ANSI.m.white,
		}
	return styles.get(a)

def txt(**k):
	"""
	examples:
	print(str(txt(txt='test',markup=[0,'green','line',0])))
	print(str(txt(txt='ikkel',markup=['blue'])))
	print(str(txt(txt='ikkel',markup=['strike',0])))
	:param k:
	:return:
	"""
	str_styles='{placeholder}'
	style_chain=k.get('markup')
	if style_chain[0]==0: #=start with reset
		style_chain=style_chain[1:]
		str_styles=str_styles.format(placeholder='{reset}{placeholder}'.format(reset=markup('reset'),placeholder='{placeholder}'))
	if style_chain[-1]==0: #=stop with reset
		style_chain=style_chain[0:-1]
		str_styles=str_styles.format(placeholder='{placeholder}{reset}'.format(reset=markup('reset'),placeholder='{placeholder}'))
	for  style in style_chain:
		str_styles=str_styles.format(placeholder='{style}{placeholder}'.format(style=markup(style),placeholder='{placeholder}'))
	reset=markup('reset')
	text=str(k.get('txt'))
	return str_styles.format(placeholder=text,reset=reset)



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
	txt_styled=txt(txt=text, markup=styles)
	def stdout_text(text):
		return str(txt_styled.format(placeholder=text))
	return stdout_text




# def table_gen(**k):
# 	style=m()
# 	title,headers,idx= [item in k.get('meta') for item in ['title','headers','idx']] if k.get('meta') else [False,False,False]
# 	data=k.get('data')
#
#
# 	if title:
# 		title=data.pop(0)
# 	if headers :
# 		headers=data.pop(0)
# 		table = ansitable.ANSITable(header=True)
# 	else:
# 		table = ansitable.ANSITable(header=False)
# 		headers=list(range(len(data[0])))
#
# 	for header in headers:
# 		header=f'{style.line}{header}'
# 		table.addcolumn(f'{header}')
#
# 	for row in data:
# 		row=[f'{style.reset}{cell}{style.reset}' for cell in row]
# 		table.row(*row)
#
# 	table.print()
#
# 	#groups sendond to last
# 	#title goes last
# 	# for header in headers:
# 	# 	table(data=header)
	
# def table(**k):
# 	headers=k.get('headers')
#
#
# 	table = ansitable.ANSITable()
# 	for header in headers:
# 		table.addcolumn(header)
#
# 	# table.row("aaaaaaaaa", 2.2, 3)
# 	# table.row("bbbbbbbbbbbbb", 5.5, 6)
# 	# table.row("ccccccc", 8.8, 9)
# 	# table.print()
#
# table_gen(meta=['headers'],data=[['title1','t2','tit3'],['aa','bb','cc'],['00','11111111111111111','22']])
# # def ANSI_table(**k):
	#
	#
	# fit=k.get('fit') #minw , maxw
	# TERM=TERM_init()
	#
	# if size :
	# 	cols,rows=size
	# else cols=len
	#


# def stdout_write(*a,**k):
# 	def write(*a,**k):
# 		sys.stdout.write(styled(*a, **k))
# 		sys.stdout.write(m('reset'))
# 		sys.stdout.flush()
# 	return write

# style_green=setstyle(style=['green'])
# style_blue=setstyle(style=['blue'])
# style_blue=setstyle(style=['red'])
# style_bold=setstyle(style=['bold'])
# style_line=setstyle(style=['line'])
# style_blink=setstyle(style=['blink'])

# def load_presets():
# 	mem= types.SimpleNamespace()
#
# 	# txt_test\
# 	mem.DONE=style_green('DONE')
# 	mem.MARK=style_green('*')
# 	mem.BUSY=style_blink(style_green('BUSY'))
# 	mem.CHECK=style_bold('Checking :')
# 	mem.PROC=style_bold('Processing :')
# 	# stdout_write(txt='test', style=['red','line'], org='tit2')
# 	return mem
# 	m=m()