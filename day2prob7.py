def problem7(limit: int) -> float:
    """function will calculate and print the average of the list
    of numbers from one to 'limit' which is a positive integer
    to be entered by a user.

    precondition: limit > 0
    
    >>>problem7(4)
    2.5

    """

    numbers = []
    n = 1
    while n <= limit:
        numbers.append(n)
        n = n + 1

    print((sum(numbers))/(len(numbers)))

limit = int(input("Please enter a positive integer: "))
problem7(limit)
            
            
