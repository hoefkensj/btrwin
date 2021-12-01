#!/usr/bin/env python
import os
from btrwin import debug as d


blacklist=['__pycache__','.git', '.idea', 'inspectionProfiles' , 'pyc']
filelist= ['.py','.conf','.dict']
def start(pkg):
	d.print(f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pkg}\' ]\t\"\"\"\n')

	
def level(x,s):
	t='    '
	child='=>'
	spacer=t+s
	return spacer

def ide(x,s):
	t='    '
	child='=>'
	spacer=t+'|'+t+s
	return spacer

def childof(child, parent):
	pass
	
def pkg_tree(path,x):
	global blacklist
	global filelist
	
	idd=1
	lvl=idd+1
	pkg=os.path.split(path)



	for c, f, s in os.walk(path, topdown=True):
		blisted=False

		def blck(pathstring,blisted):
			if not blisted :
				for bl in blacklist:
					if bl in pathstring:
						blisted=True
						break
					else:
						continue
			if blisted:
				return True
			else:
				return False
		def white(pathstring,wlisted):
			if not wlisted :
				for wl in filelist:
					if wl in pathstring:
						wlisted=True
					else:
						continue
				if wlisted:
					return  True
				else:
					return False
		if not blck(c,False):
			tabs=level(idd,'|')

			out=f'{tabs}===[/]-<{os.path.split(c)[1]}>'

			d.print(out, '\n')
			out=f'{tabs}{tabs}'
			d.print(out, '\n')
			
			
		
			
			
		for script in s:
			if not blck(script,False):
				if white(script,False):
					tstr=ide(idd,f'+')
					twig=f'{tstr}-->{script}\n'
					d.print(twig)
			idd+=1
		
		
		
		
			

		# d.print('\n')
		# d.print(str(s))
		# d.print('\n')

	# def lst_files(startpath):
	# 	for root, folders, files in os.walk(startpath):
	# 		folder_prefix = []
	# 		folder_content = []
	# 		for folder in folders:
	# 			go_inside = os.path.join(startpath, folder)
	# 			folder_prefix.append('')
	# 			folder_content.append(lst_files(go_inside))
	# 		files_lst = []
	# 		files_prefix = []
	# 		for f in files:
	# 			files_lst.append(f)
	# 			files_prefix.append('')
	# 		return {'name': root, 'files': files_lst, 'file_ext': files_prefix, 'folders': folder_content, 'folder_ext': folder_prefix}
	#
	# result = lst_files(path_folder)
	#
	# def prepend(lst, txt):
	# 	lst = ['{}{}'.format(i,txt) for i in lst]
	# 	return(lst)
	#
	# def add_txting(reslt, txt_test):
	# 	if reslt['file_ext']:
	# 		reslt['file_ext']=prepend(reslt['file_ext'],txt_test)
	# 	if reslt['folders']:
	# 		reslt['folder_ext']=prepend(reslt['folder_ext'],txt_test)
	# 		[add_txting(reslt['folders'][i],txt_test) for i in range(len(reslt['folders']))]
	#
	# def print_folder(reslt):
	# 	#prefix
	# 	f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pck}\' ]\t\"\"\"\n')
	#
	# print_folder(result)
	#

# def project_tree(d):
# 	exclude_prefixes = ('__', '.','..')  # exclusion prefixes
# 	pck=d
# 	os.chfolder(os.path.abspath(os.getcwd()))
# 	print(f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pck}\' ]\t\"\"\"\n')
# 	print(f'\t|')
# 	print(f'\n\t\--[/]-<{pck}','>')
#
# 	for folderpath, foldernames, files in os.walk(f'.', topdown=True,):
# 		path=''
# 		foldernames[:] = [foldername for foldername in foldernames if not foldername.startswith(exclude_prefixes)]
# 		#print(f'\n{txt(foldernames)}\n')
#
# 		print(f'{os.path.split(folderpath)[0] }')
			#print( '\n\t\t|', (len(path))*'\t---', '[',os.path.basename(folderpath),']\n')
		
		
	
		#for f in files:
		#	print('\r|', len(path)*'---', f, '\n')

			

			# 		break
						# 	elif d[0:2] == '__':
			# for d in folders:
			# 	print(f'd={d[0:2]}')
			#
			# 		break
			# 	else:
			# 		print(f"\t|+-/{.split('/')[-1:][0]} :")
			# 		print(f'{tabs(l)}+--/ {d}')
			# 		lif(l,files)
			

def main(pfx):
	pass
if __name__ == '__main__':
	path=os.path.abspath('btrwin')
	start(path)
	pkg_tree(os.path.abspath(path),0)

	# f'\n\t\--[/]-<{pkg}','>')