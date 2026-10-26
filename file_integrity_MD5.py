
# FILE INTEGRITY MONITORING SYSTEM USING MD5

# Import hashlib for MD5 hashing
import hashlib

# Import json to store checksums
import json

# Import os for file and folder operations
import os

# Get folder path from user
folder = input("Enter folder path to monitor: ")

# File to store checksum records
record = "checksums.json"

# Check whether checksum record exists
if os.path.exists(record):

    # Read previous checksums
    with open(record, 'r') as f:
        old = json.load(f)
else:
    # Create empty record
    old = {}

# Store current checksums
current = {}

# Check for missing files
for file in old:
    path = os.path.join(folder, file)

    # Check whether file is missing
    if not os.path.exists(path):
        print(file, ": Missing File")

# Check all files in the folder
for file in os.listdir(folder):
    path = os.path.join(folder, file)

    # Check whether it is a file
    if os.path.isfile(path) and file != record:

        # Read file and generate MD5 checksum
        with open(path, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()

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

# Update checksum record
with open(record, 'w') as f:
    json.dump(current, f, indent=4)

# Display completion message
print("Checksum record updated.")
