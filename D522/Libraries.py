# Python Libraries

# Python libraries can be installed using package managers like pip. The command
# pip install library_name is used in the CLI. For instance, the netmiko library, which is 
# commonly used in network automation, the command would be pip install netmiko

# If the library is already installed, can be upgraded using pip install --upgrade library_name

#############################################################################################

# Standard Library

# Collection of modules and packages that come preinstalled with Python
# Provides math operations, file I/O, system calls, and internet protocols. Considered standard
# because its available in every installation.

# Running a Library

# Involves importing it into a Python script and then calling its functions or classes. The
# socket library can be used for network automation tasks

# Example

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.sock_STREAM)

# Define the server and the port
server = 'hostname'
port = 80

# Connect to the server
s.connect((server, port))