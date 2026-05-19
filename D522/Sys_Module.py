# The sys module give your sctipy access to things like command -line
# arguments, the Python path, and the ability to exit cleanly

import sys     # Must be imported first

sys.argv       # A list of command-line arguments passed to the script

sys.exit(code) # Exits the script immediately. Code 0 = success, non-zero = Error

sys.path       # A list of directories Python searches for modules

sys.version    # A string with current Python version

#### sys.argv -- Command line arguments ####

# sys.argv is always a list. The first item (sys.argv[0]) is always the script name itself.
# Any arguments the user typed come after that.

# See backup.py

#### sys.exit() - Stopping a script early ####

import sys

if len(sys.argv) < 2:
    print("Usage: python backup.py ")
    sys.exit(1)     # exit with error code 1

print("Running backup on", sys.argv[1])
