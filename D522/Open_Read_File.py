# Opening and Reading a File

f = open("log.txt", "r")

contents = f.read() # reads entire file as one string
f.close()           # always close when done!

print(contents)

# The 'with' statement (closes file automatically when block ends)

with open("log.txt", "r") as f:
    contents = f.read()    # file is closed here automatically - no f.close() needed

print(contents)

# There are 3 ways to read

with open("log.txt", "r") as f:
    contents = f.read()   # entire file as one string

with open("log.txt", "r") as f:
    line = f.readline()   # one line at a time

with open("log.txt", "r") as f:
    lines = f.readlines() # list of all lines (with \n)
    



