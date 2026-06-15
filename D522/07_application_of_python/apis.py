# D522 - Working with APIs
# Demonstrates a common network automation workflow: pull a device config
# from a REST API, modify it locally, and push the changes back.

import requests
import json

url = 'http://network-device-api/config'

# Step 1: Read the current configuration from the API
response = requests.get(url)
data = response.json()

# Step 2: Persist the original config to disk as a backup
with open('config.json', 'w') as file:
    json.dump(data, file)

# Step 3: Modify the configuration in memory
data['setting'] = 'new value'

# Step 4: Save the updated config to disk
with open('config.json', 'w') as file:
    json.dump(data, file)

# Step 5: Push the updated configuration back to the device API
response = requests.put(url, data=json.dumps(data))
