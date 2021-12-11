#!/usr/bin/env python
import os
from os import makedirs
from sys import stdout
from colorama import Style,Fore
from btrwin import debug as d



def get_dirs(parent):
	dirs=[os.path.join(parent, name) for name in os.listdir(parent) if os.path.isdir(os.path.join(parent, name))]
	return dirs

def create_dtree(dic, path):
	for name, info in dic.items():
		next_path = path + "/" + name
		if isinstance(info, dict):
			makedirs(next_path)
			create_dtree(info, next_path)
	return

def sprint_table(lst_lines,tabspace=2,tabwidth=4,rownr=True):
	"""
	prints a table using stdout.write to stdout
	:param lst_lines: a list for every row  in the table  [['row1-cell1','row1-cell2'],['row2-cell1','row2-cell2']]
	:param tabspace: the number of tabs used as whitespace between collumn 0= longest cell
	:param tabwidth: the widh of the tabs to use in spaces (characters)
	:return: None
	"""
	sprint= stdout.write
	B='\033[1m'
	b='\033[0m'
	# prepend a cell with rownr to every line in lst_lines and store in lines
	lines=[[f'{idx+1}:'] + lst_lines[idx] if rownr else [lst_lines[idx]] for idx,line in enumerate(lst_lines)]
	#populate maxw_cell with 0 for every cell in line
	width_col= [0 for col in lines[0]]
	width_cells= [[len(col)for col in line] for line in lines]
	for row in width_cells:
		for idx,cel in enumerate(row):
			width_col[idx]= cel if  cel > width_col[idx] else width_col[idx]

	for line in lines:
		prow=''
		for cdx, cell in enumerate(line):
			padd= width_col[cdx]- len(cell)
			paddin = ' '*(padd+tabspace*tabwidth)
			if cell[-1]=='*':
				cell=f'{cell[0:-1]} {Fore.GREEN}*{Style.RESET_ALL}'
			cell=f'{cell}{paddin}'
			prow+=cell
		#-7 :-6 is the paace of * as the \033[0m gets appended to it
		if '*' in prow[-7:-6]:
			prow=f'{B}{prow}{b}'
		prow+='\n'
		sprint(prow)



def ls_dirs(path):
	"""
	:param path: path to directory to list
	:return: list of dirs in path
	"""
	return [os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def ls_files(path):
	"""
	:param path: path to directory to list
	:return: list of files in path
	"""
	return [os.path.join(path, name) for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
	
