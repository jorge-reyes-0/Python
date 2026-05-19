import sys

print(sys.argv)

# if run as: python backup.py /var/logs daily
# prints: ['backup.py', 'var/logs', 'daily']

script = sys.argv[0]

path = sys.argv[1]

mode = sys.argv[2]