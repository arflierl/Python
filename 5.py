def oddEven(limit: int) -> str:
    """Given a number greater than zero, called 'limit',
    function will retun a list from zero to limit and
    specify weather each number is odd or even.
    """
    n = 0
    while n <= limit:
        evenness = "EVEN"
        if n % 2 != 0:
            evenness = "ODD"
        print(str(n)+ " " + evenness)
        n += 1

limit = int(input("Enter a number greater than 0: "))
oddEven(limit)

   
