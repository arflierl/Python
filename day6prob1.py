##count() function in an inbuilt function in python programming language that returns the number of occurrences of a substring in the given string.
def letter_usage(x):
  from string import ascii_lowercase as letters
  text = f.read().lower()
  print(dict((l, text.count(l)) for l in letters))

f = open("someMoby.txt")
letter_usage(f)
f.close()