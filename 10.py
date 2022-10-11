def perfect_number(number: int):

    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    if sum(divisors) == number:
        print(number, "is a perfect number.")
    else:
        print(number, "is not a perfect number.")

number = int(input("Please enter a positive integer: "))
perfect_number(number)


             
