import csv

def csv_roundtrip(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['hostname', 'ip_address'])
        writer.writerow(['Router1', '1.1.1.1'])
        writer.writerow(['Router3', '2.2.2.2'])
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header
        for row in reader:
            print(row)

# Test your function
csv_roundtrip("network_inventory.csv")