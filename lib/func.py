#!/usr/bin/env python

import sys

def sprint(*a,**k):
	"""
	prints data to stdout using sys.stdout.write
	:param a: line / table to print
	:param k: any table[True/False] tabspace[INT] tabwidth[int] rownr[True/False]
	:return:
	"""
	#aliasses
	write = sys.stdout.write

	def table(lst_lines, tabspace=2, tabwidth=4, rownr=True ,rownr_offset=2):
		"""
		prints a table using stdout.write to stdout
		:param lst_lines:  a list for every row  in the table  [['row1-cell1','row1-cell2'],['row2-cell1','row2-cell2']]
		:param tabspace: the number of tabs used as whitespace between collumn 0= longest cell
		:param tabwidth: the widh of the tabs to use in spaces (characters)
		:param rownr: enables a column with a rownr for each row
		:param rownr_offset: total space between rownr and next column
		:return: None
		"""
		s=' '
		p=' '
		def cc_lens(lst_lines):
			#populate maxw_cell with 0 for every cell in line[0]
			def cal_lencells():
				len_cells=[]
				for i,row in enumerate(lst_lines):
					len_cell=[]
					for ii,cell in enumerate(row):
						len_cell+=[len(cell)]
					len_cells+=[len_cell]
				return len_cells
			
			wcol= [0 for col in lst_lines[0]]
			
			lencells=cal_lencells()
			for row in lencells:
				for i,cel in enumerate(row):
					wcol[i]=cel if cel>wcol[i] else wcol[i]
				
			if rownr:wcol[0]= 2+rownr_offset
			return wcol
		
		def add_rnrs():
			for idx,line in enumerate(lst_lines):
				line=[f'{idx+1}:']+[cel for cel in lst_lines[idx]]
				lst_lines[idx]=line

	# prepend a cell with rownr to every line in lst_lines and store in lines
		if rownr:add_rnrs()
		wcol= cc_lens(lst_lines)

		for i,line in enumerate(lst_lines):
			for ii,cell in enumerate(lst_lines[i]):
					cel_pad=wcol[ii]-len(cell)
					lst_lines[i][ii]=f'{cell}{s*cel_pad}'
		
		
		ptable=[]
		for i,line in enumerate(lst_lines):
			pline=''
			for ii,cell in enumerate(line):
				col_pad=s*tabspace*tabwidth
				if ii ==0 :
					col_pad=''
				pline+=f'{cell}{p*(wcol[ii]-len(cell))}{col_pad}'
			ptable+=[pline]
			
		
		for line in ptable:
			print(line)
		
			# prow=''
			# for cdx, cell in enumerate(line):
			# 	padd= width_col[cdx]- len(cell)
			# 	paddin = ' '*(padd+tabspace*tabwidth)
			# 	cell=f'{cell[0:-1]} {Fore.GREEN}*{Style.RESET_ALL}{paddin}' if cell[-1]=='*' else f'{cell}{paddin}'
			# 	prow+=cell
			# #-7 :-6 is the place of * as the \033[0m gets appended to it
			# write(f'{B}{prow}{b}\n' if '*' in prow[-7:-6] else f'{prow}\n')

	line= ''.join([ f'{arg}' for arg in a])
	table(*a) if k['table'] else write(line)
	

def dct_lookup(**k):
		try:
			return k["src"][f'{k["key"]}']
		except KeyError:
				pass