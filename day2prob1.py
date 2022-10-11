def palindrome(x):
  """funtion will accept a word and let the user know if given word
  is a palindrome or not
  """
  y = x[::-1]  ##"start at the end; count down to the beginning,
               ##stepping backwards one step at a time."
  if x != y:
    print(x, "is not a palindrome.")
  
  if x == y:
    print(x, "is a palindrome.")
  
palindrome("radar")
