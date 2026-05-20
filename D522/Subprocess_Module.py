# The subprocess module lets Python run external programs and
# shell commands. Like running ping, ls, or df from inside the script.

import subprocess 

subprocess.run()     # Runs a command and waits for it to finish

capture_output=True  # Captures stdout and stderr instead of printing them

text=True            # Returns output as a string instead of bytes

.returncode          # The exit code of the command (0=success)

.stdout              # The captured standard output as a string