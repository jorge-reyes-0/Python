# Listing a package

# Listing installed packages can be done using pip, the Python package installer. pip list is
# used in the CLI, which returns a list of all installed packages along w their versions

# To check if a specific package is installed, pip show package_name can be used.

#############################################################################################

# Installing a Package

# Packages can be installed using pip, command pip install package_name
# To install netmiko, use pip install netmiko
# Upgrading packages: pip install --upgrade netmiko
# Always ensure pip is upgraded to the latest version before installing packages

#############################################################################################

# Using a Package

# To use a python package, it must first be imported into the Python script using the import statement
# Once imported, the functions, classes, or variables defined in the package can be accessed using the
# dot notation

# Example

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.1',
    'username': 'password'
}

connection = ConnectHandler(**device)

output = connection.send_command('show ip int brief')
print(output)

connection.disconnect()

#############################################################################################

# Removing a package

# Packages can be removed using pip. pip uninstall package_name
