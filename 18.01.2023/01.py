file1 = open("./files/file.txt", "r")

reverse = "\n".join(file1.read().split("\n")[::-1])

file2 = open("./files/file1-copy.txt", "w")
for line in reverse:
	file2.write(line)

file2.write("\n")

file1.close()
file2.close()
