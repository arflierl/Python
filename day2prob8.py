def problem8(limit: int):
    """function will take a positive integer called 'limit', and will
    create and print a list of all numbers between one and 'limit'
    where each digit of these numbers is an even number.
    >>>problem8(25)
    2, 4, 6, 8, 22, 24
    Precondition: number entered by user will be a positive integer
    """
    digits = []
    answers = []
    n = 1
    while n < limit:
        digits = [int(i) for i in str(n)]
        for i in digits:
            if all((i % 2) == 0 for i in digits):
                answers.append(n)
        n = n + 1
        digits = []

    true_answers = list(set(answers))
    true_answers.sort()
    print(true_answers)
      
           
      
limit = int(input("Enter a positive integer: "))
problem8(limit)
