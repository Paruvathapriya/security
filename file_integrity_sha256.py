
# FILE INTEGRITY MONITORING SYSTEM USING SHA-256

# Import hashlib for SHA-256
import hashlib

# Import json to store checksums
import json

# Import os for file operations
import os

# Get folder path
folder = input("Enter folder path to monitor: ")

# File to store checksum records
record = "checksums_sha256.json"

# Read previous checksum records
if os.path.exists(record):
    with open(record, 'r') as f:
        old = json.load(f)
else:
    old = {}

# Store current checksums
current = {}

# Check for missing files
for file in old:
    path = os.path.join(folder, file)

    if not os.path.exists(path):
        print(file, ": Missing File")

# Check files in the folder
for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path) and file != record:

        # Generate SHA-256 checksum
        with open(path, 'rb') as f:
            checksum = hashlib.sha256(f.read()).hexdigest()

        # Store current checksum
        current[file] = checksum

        # Check for new file
        if file not in old:
            print(file, ": New File")

        # Check for unchanged file
        elif old[file] == checksum:
            print(file, ": Not Modified")

        # Check for modified file
        else:
            print(file, ": Modified")

# Update checksum records
with open(record, 'w') as f:
    json.dump(current, f, indent=4)

print("Checksum record updated.")
