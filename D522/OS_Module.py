import os        # Forgetting this will cause a NameError

print(os.getcwd())      # Returns the current working directory as a string

os.chdir(path)   # Changes the current working directory to path

os.listdir(path) # Returns a list of filenames in the given directory

#### File and Directory Operations ####

os.rename(src, dst) # Renames or moves a file

os.remove(path)     # Deletes a file

os.makedirs(path)   # Creates directories, including any missing parent dirs

os.rmdir(path)      # Removes an empty directory

#### os.path - Checking and Building Paths

os.path.join(a, b)   # Joins path parts using the correct separator for the OS

os.path.exists(path) # Returns true if path exists (file or directory)

os.path.isfile(path) # Returns true if path is a file

os.path.isdir(path)  # Returns true if path is a directory

os.path.basename(path)  # Returns just the filename from a full path