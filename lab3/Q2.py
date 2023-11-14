import os
import hashlib

# Read the expected SHA-256 hash from the Q1hash.txt file
with open('Q2hash.txt', 'r') as q2hash_file:
    expected_hash = q2hash_file.read().strip()  # Remove leading/trailing white spaces
# expected_hash = "41729bc5e7b154a9d171ff1b56da931057850134c4c30ae43e17fd9a33aa04dd"
#print(expected_hash)


# Directory containing files to hash
directory = 'Q2files'

# Iterate through files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    # Calculate the SHA-256 hash manually
    hash_obj = hashlib.sha256()
    
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64K chunks
            if not data:
                break
            hash_obj.update(data)
    
    calculated_hash = hash_obj.hexdigest()
    #print(calculated_hash)
    
    # Compare the calculated hash to the expected hash
    if calculated_hash == expected_hash:
        print(f'Match found: {filename}')
        print(f'expected hash: {expected_hash}')
        print(f'hash of {filename}: {calculated_hash}')
        break  # Exit the loop if a match is found
