import os.path, time
import pathlib
File_name=input("Enter the file path:")
l= len(File_name)
File_name=File_name.replace(File_name[0],'')
print("Name of the file : %s " % (os.path.basename(File_name)))
print("Last modified on : %s" % time.ctime(os.path.getmtime(File_name)))
print("Created on       : %s" % time.ctime(os.path.getctime(File_name)))
print("Type of the file :",pathlib.Path(File_name).suffix)
size=os.path.getsize(File_name)
mb=size/1048576 
gb=mb/1024
kb=size/1024
if(mb<1):
    print("Size of the file : {:.2f} KB".format(kb))
if(mb<1024):
    print("Size of the file : {:.2f} GB".format(gb))
else:
    print("Size of the file : {:.2f} MB".format(mb))
    