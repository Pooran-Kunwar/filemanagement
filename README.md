# filemanagement

1) We all know that to organize all these files manually, it's so boring and time taking tasks.
   That's why in this video we are going to write a Python script that automatically organizes all these files.
   
3) Let's start.

4) First of all, we need to import the required modules.
   So import OS and Shuttle module.

5) os module which provides a protable way of using operating system
   shutil module which helps in automating process of copying and removal of files or directory.
   These are inbuilt modules, so no need to install them.

6) we are using try and except block so that we can handle any error if it occurs.

7) First of all we create a variable called path which takes the input of the directory path
   now create a variable name files in wich list all the files present in the given directory.

8) Now write a for loop condition using ForLoop.
   We traverse through every file from files and splitting extention name from file.

9) then we need to write if statement, if the extension directory already exists,then we move the file to
   that directory.

10) In else statement, we make a new directory and then we move the file into it.

11) Let's run this program.And it's successfully executed.
