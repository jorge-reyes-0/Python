# Writing to an existing file can be done using the open() function with the 'a'
# or 'w' mode.'a' appends to the end of the file, while the 'w' mode overwrites the file

# Example

import os

with open('device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()
    print(device_ip)

response = os.system('ping -n 1 ' + device_ip)

with open('log.txt', 'a') as file:
    if response == 0:
        file.write(device_ip + ' is up!\n')
    else:
        file.write(device_ip + ' is down!\n')

########################################################################################

# Creating a new file

# Creating a new file can be done using the open() function with the 'x', 'a', or 'w' mode.
# 'x' creates a new file and opens it for writing. If the file exists, operation fails

# 'a' opens the file for writing, appending to the end of the file if it exists

# 'w' opens the file for writing, if the file exists it is truncated. If the file doesnt
# exist, it is created

# 'x' mode

try:
    with open('file.txt.', 'x') as file:
        file.write('Content for the new file\n')
except FileExistsError:
    print('File Already Exists')

# 'a' mode

with open('newfile.txt', 'a') as file:
    file.write('Content for the new file\n')

# 'w' mode

with open('newfile.txt', 'w') as file:
    file.write('Content for the new file\n')

# Another example

import os

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