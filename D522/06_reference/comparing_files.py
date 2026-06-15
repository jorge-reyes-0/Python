# D522 - Comparing Files with filecmp
# The filecmp module compares files and directories.
# Primary use: detect duplicate files or verify config consistency.

import filecmp   # fixed: was missing this import

# Compare two configuration files — returns True if they are identical
if filecmp.cmp('/path/to/config1.txt', '/path/to/config2.txt'):
    print('The configuration files are the same')
else:
    print('The configuration files are different.')
