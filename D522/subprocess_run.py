import subprocess

# Run a command - output goes straight to the terminal
subprocess.run(["ls", "-l"])

# Capture the output to use in your script
result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print(result.stdout)     # The commands output as a string
print(result.returncode) # 0 if successful