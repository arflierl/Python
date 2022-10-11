# Import homework 01 solutions and the formula tools.
from cse191_homework01 import generateRowLists, generateTTRows
from cse191_utils import eval_cnf_formula, load_cnf_formula


def isSatisfiable(formula_filename):
    a = load_cnf_formula(formula_filename)
    formulas = a[2]
    nbvar = a[0]
    nbargs = a[1]
    for assignment in generateRowLists(a[0]):
      #print(assignment)
      b = eval_cnf_formula(a[2], assignment)
      if b == True: 
        return True

    return False

def isTautology(formula_filename):
    a = load_cnf_formula(formula_filename)
    formulas = a[2]
    nbvar = a[0]
    nbargs = a[1]
    for assignment in generateRowLists(a[0]):
      #print(assignment)
      b = eval_cnf_formula(a[2], assignment)
      if b == False: 
        return False

    return True
