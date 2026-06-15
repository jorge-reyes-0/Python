# D522 - Reading Files
# Covers: reading plain-text config files and reading CSV files.

import csv

# ---------------------------------------------------------------------------
# Read all commands from a plain-text config file (one command per line)
def read_config_commands(config_file):
    with open(config_file, 'r') as file:
        commands = file.readlines()
    # Strip trailing newlines and whitespace from each line
    return [command.strip() for command in commands]

# ---------------------------------------------------------------------------
# CSV files
# The csv module provides csv.reader() and csv.writer() for structured data.
#
# Workflow:
#   1. open() the file in 'r' (read) or 'w' (write) mode
#   2. Pass the file object to csv.reader() or csv.writer()
#   3. next(reader) reads the header row
#   4. Remaining rows can be iterated normally

def read_device_info(device_file):
    # Use a `with` block so the file is closed automatically
    with open(device_file, 'r') as file:
        reader  = csv.reader(file)
        headers = next(reader)              # consume the header row
        devices = [row for row in reader]   # all remaining rows
    return headers, devices
