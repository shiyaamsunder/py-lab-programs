fp1 = open("./files/file4in.txt", "r")
fp2 = open("./files/file4out.txt", "w")

lines = fp1.readlines()

for line in lines:
    line = line.replace(",", ".")
    fp2.write(line)

fp1.close()
fp2.close()
