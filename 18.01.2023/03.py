fp = open("./files/file3in.txt", "r")
fp2 = open("./files/file3out.txt", "w")

lines = fp.read().split(" ")

for s in lines:
    if s.islower():
        fp2.write(s.upper())
        fp2.write(" ")

fp.close()
fp2.close()
