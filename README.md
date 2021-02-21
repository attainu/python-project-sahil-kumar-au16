
Project Submitted by Sahil Kumar



Junk File Organizer


The aim of this project is to build a python program that runs as a command-line tool. Basically, as a lazy programmer, Due to a large number of files, it is a daunting task to sit and organize each file. To make that task easy, we need a Python script that comes in handy and returns a folder where all the files are organized in a well-manner within seconds.

Table of Contents:
    • Table Of Contents

    • Technologies

    • Requirements

    • Setup

    • Steps involved

    • Output


Technologies:
    • Python



Requirements:
    • ● File handling in python

    • ● Use of OS , Shutil and date time module



Setup:

To run this project

    • Clone the repo

    • Install python

    • Import all the library functions required

    • Create folder, each folder will represent the name and details of the files

    • Run and copy the path of the desired folder where you want to modify folders extension.py to organize files by file extension, size.py to see the file size and date.py to organize files by date where files are created in a folder.



Steps Involved
    • Import all the library functions required like os,shutil and datetime

    • Create different folders based on type of files users can divided into different folders using dictionaries
    • Each folder will represent the name of the files present inside it

Organize by extension:
    • Create a function to filter file types into their respective folders

    • Use os module of python to recursively list out all the files that are present in the folder into the newly created folder.

    • Users can organize files by file extension in a given folder, folder will be created according to file extension and finally all files will be moved to a created folder.

Organize by Size:

    • create a function to get the folder path from users and create a dictionary with file size and sort the dictionary
    • users can organize files by size of file in a given folder

    • Sort the dictionary by size and prints file names and size

Organize by Date:
    • Create a function to sort files by date into their respective folders

    • Use os module of python to recursively list out all the files that are present in the folder into the newly created folder.

    • Users can organize files by date of file created in a given folder, folder will be created according to dates of files present and all files are moved to created folder
Output

Before running the code the files are shown below
After running:
