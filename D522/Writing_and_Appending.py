with open("report.txt", "w") as f:
    f.write("System check complete\n")   # overwrites file

with open("log.txt", "a") as f:
    f.write("New entry added\n")         # adds to end of file

# Unlike print(), f.write() does NOT add a newline automatically. You must use \n yourself