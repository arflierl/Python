def multiplication_table(n: int) -> None:
    """Print the multiplicaton table for numbers 1 through n inclusive.
    """

    numbers = list(range(1, n + 1))
    #Print the header row.
    for i in numbers:
        print("\t" + str(i), end="")

    # End the header row.
    print()

    #Print each row number and the contents of each row.
    for i in numbers:
        print(i, end="")
        for j in numbers:
            print("\t" + str(i * j), end="")

    #End the current row.
    print()
                  
multiplication_table(5)

    
