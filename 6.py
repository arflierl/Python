def sum_of_multiples(limit: int):
    """Precondition: 'limit' is an integer.
    function will return the sum of multiples
    of 3 and 5 between 0 and given integer
    called 'limit'.
    """
    sum = 0
    n = 1
    while (3 * n) <= limit:
        if (3 * n) % 15 != 0: 
            sum = sum + (3 * n)           
        n = n + 1
        
    n = 1
    while (5 * n) <= limit:
        sum = sum + (5 * n)
        n = n + 1
        
    print(sum)    
    return sum

limit = int(input("Enter an integer: "))
sum_of_multiples(limit)

    
    
