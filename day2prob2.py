def fibonacci_sequence(limit):
    """Function will print all Fibonacci numbers less than or
    equal to the given limit, which will be a positive integer.
    """

    n = 1
    m = 1
    x = n + m
    sequence = []
    if m == 1:
        n = 1
        x = n + m
        sequence.append(n)
        sequence.append(m)
        sequence.append(x)

    n = 1
    m = 2
    while x < limit:
        if m > 1:
            x = n + m
        if x < limit:
            sequence.append(x)            
        n = m
        m = x

    print(sequence)


limit = int(input("Enter a positive integer: "))
fibonacci_sequence(limit)
        
   
            
        
        
        
