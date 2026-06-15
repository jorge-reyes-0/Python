# The filecmp module in Python is a utility for comparing files and directories
# Primary use is in searching for duplicate files and in comparing directory trees

# Compare two configuration files

if filecmp.cmp('/path/to/config1.txt', '/path/to/config2.txt'):
    print('The configuration files are the same')
else:
    print('The configuration files are different.')