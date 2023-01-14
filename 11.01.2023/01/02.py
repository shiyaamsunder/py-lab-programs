import functools


nums = range(1, 11)

result = functools.reduce(lambda x, y: x+y, nums)

print(result)
