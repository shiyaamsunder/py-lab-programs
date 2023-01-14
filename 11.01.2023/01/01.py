chars = ['a', 'b', 'c', 'd', 'e']


def convert_to_ascii(chars):
    return list(map(lambda x: ord(x), chars))


print(convert_to_ascii(chars))
