def prime_number_test(limit: int):
    """function will take an integer number and return
    'True' if the number is a prime number, and 'False'
    if the number is not a prime number.
    """
    if limit == 0:
        print(False)
    elif limit == 1:
        print(False)
    elif limit == 2:
        print(True)
    else:
        answer = True
        n = 2    
        while n <= (limit//2):
        
            if limit % n == 0:
                answer = False
            n = n + 1

        print(answer)
    
    
limit = int(input("Enter an integer: "))
prime_number_test(limit)
