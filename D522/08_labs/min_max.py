def speed_bounds(port_speeds):
    return max(port_speeds), min(port_speeds)

# Test your function
speeds = [100, 10000, 1000, 100, 10000, 1000, 100]
high, low = speed_bounds(speeds)
print(f"Max: {high} | Min: {low}")