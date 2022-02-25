#!/usr/bin/env python
import shutil
import time
import sys
def fn(fn):
	def ansi(SEQ):
		def ANSIseq(ESC='\033', SEQ='{SEQ}', FN='{FN}'):
			return '{ESC}[{SEQ}{FN}'.format(ESC=ESC,SEQ=SEQ,FN=FN)
		return ANSIseq(SEQ=SEQ,FN=fn)
	return ansi



ANSI_E= fn('E')
ANSI_F= fn('F')
ANSI_G= fn('G')
ANSI_H= fn('H')
ANSI_K= fn('K')




def tabledata_width(**k):
	flags=k.get('flags')
	#sym shrink idx mark
	pass
	
def terminal_width(stored=[0,]):
	width=(shutil.get_terminal_size()[0]-2)
	stored+=[width]
	diff=(-1*(stored[-2]-stored[-1]))
	print(stored[-2],stored[-1],diff)

terminal_width()



table={
		'T' : [['title'],['subtitle']],
		'H'	:	['idx','header1','header2'],
		'M'	:	{'dltr'	: '|','pad'	: '    '},
		'D'	:	[
					[1,'dat444545888a1','da1ta2'],
					[55582,'data1','r'],
					[3,'r','data52'],
					],
		'F'	:	[['help'],['footer']]
	}
cols={}

# width=[0 for i in  range(len(table['D'][0]))]
# for a in range(len(table['D'][0])):
# 	for i in range(len(table['D'])):
# 		sys.stdout.write(f"{len(str(table['D'][a][i]))}")
# 		width[i]=len(str(table['D'][a][i])) if width[i]< len(str(table['D'][a][i])) else width[i]


def table_dimentions(**k):
	def strw(a,i):
		return len(str(table['D'][a][i]))
	tbl_titles=k.get('tbl')['T']
	tbl_headers=k.get('tbl')['H']
	tbl_footers=k.get('tbl')['F']
	tbl_data=k.get('tbl')['D']
	dltr=k.get('tbl')['M'].get('dltr')
	pad=k.get('tbl')['M'].get('pad')
	lst_colwidths=[0 for item in tbl_headers]
	for a,_ in enumerate(table['D'][0]):
		for i,_ in enumerate(table['D']):
			lst_colwidths[i]=max(strw(a,i) ,lst_colwidths[i])
	lst_colwidths=[colw+len(dltr)+len(pad*2) for colw in lst_colwidths]
	
	tbl_w=sum(lst_colwidths)
	titw=divmod(tbl_w,len(tbl_titles))[0]
	x_tits=[0 for i in tbl_titles]
	x_tits= [1+(n*titw) for n,i in enumerate(x_tits)]
	tmp_hds=[0, *lst_colwidths]
	x_hds=[0 for item in lst_colwidths]
	for  n,i in enumerate(lst_colwidths):
		if n == 0 :
			x_hds[n]=1
		else:
			x_hds[n]=x_hds[n-1]+tmp_hds[n]
	return x_hds

print(repr(table_dimentions(tbl=table)))
# print(cols)
# import sys
# unic=''
# sys.stdout.write(unic)
# ansi='\033[{code}'.format(code='32m')
# sys.stdout.write(ansi)
# sys.stdout.write('test')


# def list_descend(data,lasts=[]):
# 	for item in data:
# 		if isinstance(item,list):
# 			list_descend(item)
# 		else:
# 			lastset+=item
# 		lasts+=lastset
# 		lastset=[]
# 	return lasts
	

# desc=list_descend(table)
# print(desc)
def lister(data,rows=[]):
	
	if isinstance(data,list):
		itemset=[]
		for item in data:
			if isinstance(item,list):
				lister(item)
			else:
				itemset+=[str(item)]
		rows+=[itemset]
	return rows
rows=lister(table)

# [print(row) for row in rows]
# print()
# print()

upper = [chr(i) for i in range(65, 91)]
lower = [chr(i) for i in range(96, 123)]
# [sys.stdout.write(chr(i)) for i in range(65, 91)]
enumerate(table)
# def alfa(val):

#
# print(ord('A'))