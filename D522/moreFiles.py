# Closing a file can be done using the close() method

file = open('filename.txt', 'r')
file.close()

# Closing files in python is necessary for the following reasons:
    # It frees up system resources that were tied to the file

    # It ensures that changes made to the file are saved. Some changes made to a file
    # in Python may not be immediately written to disk; closing the file ensures that 
    # changes are not lost

    # It prevents further modifications to the file. Once a file is closed, attempting to 
    # write to it will produce an error

# Checking for file existence

# Checking for file existence can be done using the os.path.exists() function from the os module

import os

file_path = 'filename.txt'

if os.path.exists(file_path):
    print('The file exists')
else:
    print('File doesnt exist')

# Deleting files and Folders

# Can be done using the remove() function from the os module

import os
file_path = 'filename.txt'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('The file does not exist')

# Deleting a folder can be done using the rmdir() function from the os module

import os

folder_path = 'foldername'

if os.path.exists(folder_path):
    os.rmdir(folder_path)
else:
    print('The folder does not exist')