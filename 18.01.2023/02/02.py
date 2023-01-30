import math
try:
  x = int(input("Enter a number: "))

  assert x > 0, "Number cannot be negative"
  print(math.sqrt(x))


except AssertionError as msg:
  print(msg)

