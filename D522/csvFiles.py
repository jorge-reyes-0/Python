# For CSV files, Python provides the csv module to read and write CSV files

# Opening a file
    # Use the open() function with the filename and mode as arguments.
    # The 'r' mode is for reading, and 'w' is for writing
# Creating a CSV reader or writer
    # Use the csv.reader() or csv.writer() function to create a reader or writer
# Reading from a file
    # Use the next() function to read a row from the file. Each row is returned as
    # a list of strings
# Writing to a file
    # Use the writerow() function to write a row to the file. The row should be a
    # list of strings

# Example

import csv

def read_device_info(device_file):
    # Open the file in read mode
    file = open(device_file, 'r')

    # Create a CSV Reader
    reader = csv.reader(file)

    # Read the header row
    headers = next(reader)

    # Read the rest of the rows
    devices = [row for row in reader]

    # Close the file
    file.close()

    return headers, devices