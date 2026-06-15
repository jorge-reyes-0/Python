# D522 - Python Packages
# A package is a directory of modules. Install packages with pip.

# ---------------------------------------------------------------------------
# pip commands (run in your terminal)
#
#   pip list                        — list all installed packages with versions
#   pip show <package_name>         — details for a specific package
#   pip install <package_name>      — install a package
#   pip install --upgrade <pkg>     — upgrade to the latest version
#   pip uninstall <package_name>    — remove a package
#
# Always upgrade pip itself before installing packages:
#   pip install --upgrade pip

# ---------------------------------------------------------------------------
# Using an installed package — netmiko example
# Import the class you need, then pass device details as a dict.

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip':          '10.0.0.1',
    'username':    'admin',
    'password':    'password',
}

connection = ConnectHandler(**device)
output = connection.send_command('show ip int brief')
print(output)
connection.disconnect()
