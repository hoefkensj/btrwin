#!/usr/bin/env python
from os import makedirs
from sys import stdout

def create_dtree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			makedirs(next_path)
			create_dtree(info, next_path)
	return

def sprint_table(lst_lines,tabspace=2,tabwidth=4,rownr=False):
	"""
	prints a table using stdout.write to stdout
	:param lst_lines: a list for every row  in the table  [['row1-cell1','row1-cell2'],['row2-cell1','row2-cell2']]
	:param tabspace: the number of tabs used as whitespace between collumn 0= longest cell
	:param tabwidth: the widh of the tabs to use in spaces (characters)
	:return: None
	"""

	sprint= stdout.write
	max_col=[]
	col_width=[]
	for line in lst_lines:
		max_col+=[0 for col in enumerate(line)]
		max_col= [len(line[idx]) if len(line[idx]) > max_col[idx] else max_col[idx] for idx ,col in enumerate(line)]
	col_width= [( divmod(col,4)[0]+tabspace)*tabwidth for col in  max_col]
	
	for idx,line in enumerate(lst_lines):
		if rownr:
			sprint(f'{idx}: ')
		for idx,item in enumerate(line):
			tabs= divmod(col_width[idx]-len(item),tabwidth)
			tabs= tabs[0]+1 if tabs[1] > 0 else tabs[0]
			padd = '\t'*tabs
			cell=f'{item}{padd}'
			sprint(cell)
		sprint('\n')
		

