# D522 - SSH Automation with Paramiko
# Demonstrates connecting to a network device over SSH and running commands
# from a configuration file.

import paramiko

def automate_config(device_ip, username, password, config_file):
    ssh = paramiko.SSHClient()
    # AutoAddPolicy trusts unknown host keys — acceptable in a lab environment.
    # In production, load known_hosts instead.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(device_ip, username=username, password=password)

        with open(config_file, 'r') as file:
            commands = file.read().splitlines()

        for command in commands:
            ssh.exec_command(command)
    finally:
        # Always close the connection, even if an exception occurs
        ssh.close()
