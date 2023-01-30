try:
  x = int(input("Enter a number:"))
  y = int(input("Enter another number:"))
  assert x > y, "First number must be greater than second"
  print(min(x, y))

# the errror_message provided by the user gets printed
except AssertionError as msg:
	print(msg)
