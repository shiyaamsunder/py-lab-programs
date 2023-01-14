some_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'v': 1}


def remove_dup(_dict):
    res = {}
    for key, value in _dict.items():
        if value not in res.values():
            res[key] = value

    return res

print(remove_dup(some_dict))
