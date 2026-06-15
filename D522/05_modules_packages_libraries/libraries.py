# D522 - Python Libraries
# Libraries extend Python with pre-built functionality.
# Install them with pip; then import and use them in any script.

# ---------------------------------------------------------------------------
# Installing libraries (run these in your terminal, not in Python)
#
#   pip install netmiko
#   pip install --upgrade netmiko
#   pip list                     # list all installed packages
#   pip show netmiko             # show details for a specific package

# ---------------------------------------------------------------------------
# Standard Library — ships with Python, no installation required.
# The socket module is commonly used in network automation.

import socket

# Create a TCP socket (SOCK_STREAM = TCP, SOCK_DGRAM = UDP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # fixed: was socket.sock_STREAM

server = 'hostname'
port   = 80
s.connect((server, port))
