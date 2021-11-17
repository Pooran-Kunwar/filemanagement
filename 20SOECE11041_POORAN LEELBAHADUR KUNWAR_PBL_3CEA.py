#import os module which provides a protable way of using operating system 
import os

#import shutil module which helps in automating process of copying and removal of files or directory
import shutil
try:

    #create a variable called path which takes the input of the directory path
    path = input (r"Enter the Path : ")

    #listing all the files present in the directories 
    files = os.listdir(path)

    for file in files :
        #spliting extention
        filename,extention = os.path.splitext(file)
        extention = extention[1:]

        #if directory exits then move the files in the directory
        if os.path.exists(path+"/"+extention):
            shutil.move(path+"/"+file, path+"/"+extention+"/"+file)

        #if directory dones't exits then make a directory and move the files 
        else:
            os.makedirs(path+"/"+extention)
            shutil.move(path+"/"+file, path+"/"+extention+"/"+file)

#if any error occurre then this blocks excutied
except Exception as a:
     print("an error occurred")
     