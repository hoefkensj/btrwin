#!/usr/bin/env python
import os,sys
from btrwin import debug as d


blacklist=['__pycache__','.git', '.idea', 'inspectionProfiles' , 'pyc']
filelist= ['.py','.conf','.dict']
def faailed():

 def project_tree(d):
  exclude_prefixes = ('__', '.','..')  # exclusion prefixes
  pck=d
  os.chfolder(os.path.abspath(os.getcwd()))
  print(f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pck}\' ]\t\"\"\"\n')
  print(f'\t|')
  print(f'\n\t\--[/]-<{pck}','>')

  for folderpath, foldernames, files in os.walk(f'.', topdown=True,):
    path=''
    foldernames[:] = [foldername for foldername in foldernames if not foldername.startswith(exclude_prefixes)]
    print(f'\n{txt(foldernames)}\n')

    print(f'{os.path.split(folderpath)[0] }')
			print( '\n\t\t|', (len(path))*'\t---', '[',os.path.basename(folderpath),']\n')



		for f in files:
			print('\r|', len(path)*'---', f, '\n')



		  break
				  elif d[0:2] == '__':
		for d in folders:
		print(f'd={d[0:2]}')
		
		  break
		else:
		  print(f"\t|+-/{.split('/')[-1:][0]} :")
		  print(f'{tabs(l)}+--/ {d}')
		  lif(l,files)
		n=4

	def folder(current,l,n):
		branch='===[/]-<'
		prefix=f"{ident(l,'f',n)}{branch}{current}>"
		return prefix

	def script(current,l,n):
		branch='--< '
		prefix=f"{ident(l,'s',n)}{branch}{current}"
		return prefix

	def tab(n):
			t=' '
			ts= t+t+t+t
			return ts

	def level(sep,n):
		""""tab + sepaarator  """
		lev=f'{tab(n)}{sep}'
		return lev

	def start(pkg):
		strt= f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pkg}\' ]\t\"\"\"\n'
		return strt


	def ident(l,type,n):
		if type == 's'	:
			splice = '+'
		else :
			splice = '|'

		if l == 1:
				sep ='|'
				idd= level(sep,n)
				prefix = idd
		else:
			idd=level('|',n)
			idds=idd*(l)
			prefix=idds+level(splice,n)
		return prefix

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
				for wl in filelist:
					if wl in pathstring:
						wlisted=True
					else:
						continue
					ret = [True if wlisted  else False]
					return ret

	def recurse(c,s,lvl,n):
		if not blck(c,False):
			out=folder(os.path.split(c)[1],lvl,n)
			lvl+=1
			print(out)

			for scr in s:
				if not blck(scr,False):
					if white(scr,False):
						out=script(os.path.split(scr)[1],lvl,n)
						print(out)

		return lvl
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

	def pkg_tree(path,x):
		global blacklist
		global filelist
		global n
		prev=path
		lvl=1
		pkg=os.path.split(path)
		for c, f, s in os.walk(path, topdown=True):
			if os.path.split(c)[0] == prev:
				prev=c

				lvl=lvl=1
			else:
				lvl=lvl-1
			blisted=False
			lvl = recurse(c,s,lvl,n)




			 def white(pathstring,wlisted):
			  if not wlisted :
			    for wl in filelist:
			      wlisted=[True if wl in pathstring else False]
			    return wlisted
			 d.print('\n')
			 d.print(str(s))
			 d.print('\n')

		 def lst_files(startpath):
		  for root, folders, files in os.walk(startpath):
		    folder_prefix = []
		    folder_content = []
		    for folder in folders:
		      go_inside = os.path.join(startpath, folder)
		      folder_prefix.append('')
		      folder_content.append(lst_files(go_inside))
		    files_lst = []
		    files_prefix = []
		    for f in files:
		      files_lst.append(f)
		      files_prefix.append('')
		    return {'name': root, 'files': files_lst, 'file_ext': files_prefix, 'folders': folder_content, 'folder_ext': folder_prefix}
		
		 result = lst_files(path_folder)
		
		 def prepend(lst, txt):
		  lst = ['{}{}'.format(i,txt) for i in lst]
		  return(lst)
		
		 def add_txting(reslt, txt_test):
		  if reslt['file_ext']:
		    reslt['file_ext']=prepend(reslt['file_ext'],txt_test)
		  if reslt['folders']:
		    reslt['folder_ext']=prepend(reslt['folder_ext'],txt_test)
		    [add_txting(reslt['folders'][i],txt_test) for i in range(len(reslt['folders']))]
		
		 def print_folder(reslt):
		  prefix
		  f'\n#=>[~]\t\"\"\"\tPackage: [ \'{pck}\' ]\t\"\"\"\n')
		
		 print_folder(result)
			