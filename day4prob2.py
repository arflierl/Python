def get_divisors(x: int):

    divisors = [1]
    for i in range(2, x):
        if (x % i)==0:
            divisors.insert(len(divisors), i)
    print(divisors)
    run = True
    while run == True:
        
        y = input("type 'c' to continue or 'q' to quit: ")
        if y == "c":
            x = int(input("Please enter an integer: "))
            get_divisors(x)
        elif y == "q":
            print("Exiting program...come back soon! ")
            run == False
            break
        else:
            print("Error: please type 'c' to continue, or 'q' to quit.")
        

        
get_divisors(int(input("Please enter an integer: ")))

   
