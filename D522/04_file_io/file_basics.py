# D522 - File Basics
# Covers: open modes, built-in file functions, closing files,
#         checking for file existence, and deleting files/folders.

import os

# ---------------------------------------------------------------------------
# Built-in file functions reference
#
#   open(filename, mode)   — modes: 'r' read, 'w' write, 'a' append, 'b' binary
#   file.read([size])      — read up to `size` bytes (or entire file if omitted)
#   file.readline()        — read the next line
#   file.readlines()       — return all lines as a list
#   file.write(string)     — write string, returns number of characters written
#   file.close()           — flush and release the file handle

# ---------------------------------------------------------------------------
# Closing a file manually (prefer `with` blocks — they close automatically)
file = open('filename.txt', 'r')
file.close()

# ---------------------------------------------------------------------------
# Check whether a file exists before acting on it
file_path = 'filename.txt'

if os.path.exists(file_path):
    print('The file exists')
else:
    print("File doesn't exist")

# ---------------------------------------------------------------------------
# Delete a file (only if it exists to avoid an error)
file_path = 'filename.txt'

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('The file does not exist')

# ---------------------------------------------------------------------------
# Delete an empty folder
folder_path = 'foldername'

if os.path.exists(folder_path):
    os.rmdir(folder_path)
else:
    print('The folder does not exist')
