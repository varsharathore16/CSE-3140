"""
    First write a Python script, Q1A.py, that reads the files in the current (working) directory, 
    and outputs a file containing the names of all .py files, each on a separate line. 
    Your program should work on both Linux and Windows; 
    you may want to read about, and possibly use, the Lib/os.py library.  
    On the VM, place the completed program in directory Lab2/Solutions (with name Q1A.py). 
"""
    
import os

# Get the current working directory
current_directory = os.getcwd()

# Create a list to store the names of .py files
py_file_names = []

# Iterate over all files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".py"):
        py_file_names.append(filename)

# Create a new file to write the output
output_filename = "Q1Anames.txt"
print("List of .py files has been written to", output_filename)

with open(output_filename, "w") as output_file:
    for py_file_name in py_file_names:
        output_file.write(py_file_name + "\n")
        print(py_file_name)

#######################