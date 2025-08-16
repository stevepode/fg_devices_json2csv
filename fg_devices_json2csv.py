# ---
# Converts a FortiGate JSON device list into a CSV file
# Exports key device details: MAC, IP, hostname, interface, OS, and last seen timestamp
# ---
# Stefano Podestà - 25/07/2025
# Ver. 1.0
# MIT License
# ---

import json
import csv
from datetime import datetime

# Load JSON data from file (API response from FortiGate)
with open('fortigate_devices.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Retrieve the list of devices from the JSON "results" key
devices = data.get('results', [])

# Define CSV columns to export
fields = ['mac', 'ipv4', 'hostname', 'detected_interface', 'os_name', 'last_seen_readable']

# Convert UNIX timestamp to a human-readable string
def convert_timestamp(ts):
    try:
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ''

# Open the CSV file for writing and export device data
with open('fortigate_devices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    # Iterate over each device and write its details to the CSV
    for dev in devices:
        row = {
            'mac': dev.get('mac', ''),
            'ipv4': dev.get('ipv4', ''),
            'hostname': dev.get('hostname', ''),
            'detected_interface': dev.get('detected_interface', ''),
            'os_name': dev.get('os_name', ''),
            'last_seen_readable': convert_timestamp(dev.get('last_seen', 0))
        }
        writer.writerow(row)

print("CSV file 'fortigate_devices.csv' created successfully.")
