
# DO NOT PUT ANY TESTS/INPUT/PRINT STATEMENTS IN THIS FILE
# AS IT MAY PRODUCE ERRORS GRADING YOUR CODE. TESTING SHOULD
# BE DONE FROM THE MAIN FILE.

# You may not add any additional import statements.
import cse191_utils

# Provided the input_set, as a list of values (order doesn't matter),
# produce a new list containing every possible subset of input_set 
# (again, order doesn't matter).

            
    
def generate_powerset(input_set):
  # Code will not be graded without the following:
  # Name: Aaron Flierl
  # UBIT: arflierl
  power_set = []
  
  def generateTTRows(n: int):
      v = ["F"] * n 
      power_set.append([])
      while v != (["T"] * n):
          k = "".join(v).rfind("F")
          v[k] = "T"
          for i in range(k + 1, n):
              v[i] = "F"
          temp = []
          for i in range(0, len(input_set)):
            if v[i] == "T":
              temp.append(input_set[i])
          power_set.append(temp)

  generateTTRows(len(input_set))
  
  return power_set
