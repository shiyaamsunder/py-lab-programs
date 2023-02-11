import re
fp = open("./files/file2.txt")

pattern = "print"
lines = fp.read().split("\n")
for line in lines:
	if re.search(pattern, line):
		print(line)
 
fp.close()
