# D522 - Writing Files
# Covers: append mode ('a'), overwrite mode ('w'), and exclusive-create mode ('x').

import os

# ---------------------------------------------------------------------------
# 'a' mode — append to an existing file (or create it if it doesn't exist)
# Reads a device IP from a file, pings it, and logs the result.

with open('device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()

response = os.system('ping -n 1 ' + device_ip)

with open('log.txt', 'a') as file:
    if response == 0:
        file.write(device_ip + ' is up!\n')
    else:
        file.write(device_ip + ' is down!\n')

# ---------------------------------------------------------------------------
# File creation modes
#
#   'x' — create new file; raises FileExistsError if it already exists
#   'a' — open for appending; creates the file if it doesn't exist
#   'w' — open for writing; truncates if the file exists, creates if it doesn't

# 'x' mode — safe for first-time file creation
try:
    with open('file.txt', 'x') as file:   # fixed: was 'file.txt.' (trailing dot)
        file.write('Content for the new file\n')
except FileExistsError:
    print('File already exists')

# 'a' mode
with open('newfile.txt', 'a') as file:
    file.write('Content for the new file\n')

# 'w' mode — overwrites any existing content
with open('newfile.txt', 'w') as file:
    file.write('Content for the new file\n')

# ---------------------------------------------------------------------------
# Combined example — ping and log, using 'x' to avoid overwriting old logs
with open('device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()

response = os.system('ping -n 1 ' + device_ip)

try:
    with open('newtxt.txt', 'x') as file:
        if response == 0:
            file.write(device_ip + ' is up!\n')
        else:
            file.write(device_ip + ' is down!\n')
except FileExistsError:
    print('Log file already exists.')
