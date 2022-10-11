"""Problem 5:  Write a function that allows the user to enter test scores
using a while loop.  When the user enters "done" the function will print
out the total score and the average score.
"""

def test_scores():
    #Precondition: scores entered are in range(0, 101)
    scores = []
    n = 0
    score = ""
    
    while score != "done":
        score = input("Enter test score or type 'done' to quit: ")
        if score != "done":
            scores.append(score)
            n = (n + 1)
        elif score == "done":
            scores = list(map(int, scores))  
            print("The total score is: ", sum(scores))
            print("The average score is: ", (sum(scores) / n))
       
test_scores()
