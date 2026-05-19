# The sys module give your sctipy access to things like command -line
# arguments, the Python path, and the ability to exit cleanly

import sys     # Must be imported first

sys.argv       # A list of command-line arguments passed to the script

sys.exit(code) # Exits the script immediately. Code 0 = success, non-zero = Error

sys.path       # A list of directories Python searches for modules

sys.version    # A string with current Python version