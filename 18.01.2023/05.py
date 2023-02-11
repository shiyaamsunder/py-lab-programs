fp1 = open("./files/file5in.txt", "r+")
fp2 = open("./files/file5out.txt", "r+")

a = fp1.read()
b = fp2.read()

fp1.seek(0)
fp1.truncate()

fp2.seek(0)
fp2.truncate()

fp1.write(b)
fp2.write(a)

fp1.close()
fp2.close()
