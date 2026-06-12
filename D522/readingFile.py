def read_config_commands(config_file):
    # Open the file in read mode
    file = open(config_file, 'r')

    # Read all lines into a list
    commands = file.readlines()

    # Close the file
    file.close()

    # Remove newline characters
    commands = [command.strip() for command in commands]

    return commands