local_path = '/var/www/vserv'
destination_path = r'/home/ankur/Desktop/SugarCRM-OTRS-Integration/SugarCRM/vserv'
import os
import shutil
from filecmp import dircmp
def print_diff_files(dcmp):
	for name in dcmp.diff_files:
		print "diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right)
		shutil.copy2(dcmp.left+'/'+name, dcmp.right)
	for sub_dcmp in dcmp.subdirs.values():
		print_diff_files(sub_dcmp)
	for left_file in dcmp.left_only:
#		print (left_file, dcmp.left, dcmp.right)
		if os.path.isfile(dcmp.left+'/'+left_file):
			shutil.copy2(dcmp.left+'/'+left_file, dcmp.right)
			print('Is Fileeeeee - '+dcmp.left+'/'+left_file+"\n")
		if os.path.isdir(dcmp.left+'/'+left_file):
			os.makedirs(dcmp.right+'/'+left_file)
			print('Is Dirrrrrr'+dcmp.left+'/////////////////'+left_file+"\n")

dcmp = dircmp(local_path, destination_path, ignore=['cache',r'.git',r'.log','sugar_logs']) 
print_diff_files(dcmp) 




#for (dirpath, dirnames, filenames) in walk(mypath):
#	for file_nm in filenames:
#		
#	print(filenames)
#	print ("\n\n")
#	break
#import filecmp
#a =  filecmp.dircmp('/var/www/info', '/home/ankur/Desktop/info')
#print(a)
#if not os.path.exists(directory):
#os.makedirs(directory)

