# Python provides several built-in functions for handling files, here are some key functions:

open(filename, mode): # Opens a file in the specified mode ('r' for read,'w' for write, 'a'
                      # for append, 'b' for binary)

file.read([size]): # Reads at most size bytes from the file. If size is not specified, reads the whole file

file.readline(): # Reads the next line of a file

file.readlines(): # Returns a list of all lines in a file

file.write(string): # Writes the string to the file and returns the number of characters written

file.close(): Closes the file