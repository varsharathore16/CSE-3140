import sys

print("Hello World")

with open('Q1B.out', 'a') as log_file:
    log_file.write(' '.join(sys.argv) + '\n')

#virus end