import re
f1 = open("./files/file6in.txt", "r")

lines = f1.read()
def replace_func(match):
    if match.group(1) is not None:
        return "[" + str(match.group(1)) + "]"
    if match.group(2) is not None:
        return match.group(2).upper()
x = re.sub(r"([0-9])|(\. \w)", replace_func, lines)

print(x)


f1.close()
