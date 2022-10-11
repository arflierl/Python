def sort(x: float, y: float, z: float):

    """Function will take three user entered numeric arguments
    and print them in numberic order

    >>>sort(-134, 1, 234)
    -134, 1, 234
    >>>sort(0, 234, 1)
    0, 1, 234

    """
    arguments = []
    arguments.append(x)
    arguments.append(y)
    arguments.append(z)
    arguments.sort()
    print(arguments)


x = float(input("Please enter a number: "))
y = float(input("Please enter a number: "))
z = float(input("Please enter a number: "))
sort(x, y, z)

    
              
    
