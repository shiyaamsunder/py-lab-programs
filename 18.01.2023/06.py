import re
f1 = open("./files/file6out.txt", "w")

data = "This data contains some data. every character after the fullstop is captialised. and the numbers like 5 are bracketed.\n"


def replace_func(m):
    return f"{m.expand(r'\1GAR')}"

x = re.sub(r"([0-9])|(\.)", replace_func, data)

#print(x)


f1.close()
