def compute(x, y):
    if x<=y:
        return 0
    return compute(x-y, y) + 1

print(compute(10, 5))

