import paramiko

def automate_config(device_ip, username, password, config_file):
    # Create SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the network device
    ssh.connect(device_ip, username=username, password=password)

    # Open the configuration file
    with open(config_file, 'r') as file:
        commands = file.read().splitlines()
    
    # Execute each command
    for command in commands:
        ssh.exec_command(command)
    
    # Close the connection
    ssh.close()