def words_backwords(x):
  """function will take a phrase of several words and will
  return the phrase with the words (not letters) backwards
  """
  x = x.split() #To split a string into an array
  x.reverse()	#To reverse the array
  print(x)

words_backwords("Alabama is a beautiful state!")

