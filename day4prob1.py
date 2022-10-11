def make_a_list(x: int):

    nums = []
    odds = []
    y = ""
    run = True
    nums.append(x)
    
    while run == True:
        y = input("Type 'c' to continue adding numbers to your list " +
                  "or type 'q' to quit and print a list of the odd " +
                  "numbers you have entered: ")
        if y == "c":
            x = int(input("Enter a number: "))
            nums.append(x)
        elif y == "q":
            run == False
            break
        else:
            print("Error: please type either 'c' or 'q'!")

    for i in nums:
        if i % 2 != 0:
            odds.append(i)

    print(odds)
    return odds

make_a_list(int(input("Enter a number: ")))

            
              
        
        


