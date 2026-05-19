import os

log_dir = "/var/logs"
backup_dir = "/var/backups"

# Only create backup dir if it doesn't exist yet
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Loop through all files in the log directory

for filename in os.listdir(log_dir):
    src = os.path.join(log_dir, filename)
    dst = os.path.join(backup_dir, filename)
    if os.path.isfile(src):
        os.rename(src, dst)
        