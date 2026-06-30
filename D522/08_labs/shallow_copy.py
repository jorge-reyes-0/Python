def clone_config(config):
    copied_dict = config.copy()
    copied_dict['backup'] = True

    return config, copied_dict

# Test your function
original = {"hostname": "core-sw-01", "vlan": 10, "location": "DataCenter-A"}
orig, copy = clone_config(original)
print(orig)
print(copy)