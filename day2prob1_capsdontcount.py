def palindrome(x: str):
  """funtion will accept a word and let the user know if given word
  is a palindrome or not
  """

  
  y = x[::-1]  ##"start at the end; count down to the beginning,
               ##stepping backwards one step at a time."
  x = x.upper()
  y = y.upper()
  if x != y:
    print(x, "is not a palindrome.")
  
  if x == y:
    print(x, "is a palindrome.")
  

x = str(input("Enter a word: "))
palindrome(x)
