def print_prime_numbers(number: int):

    print(2)
    import math
    for num in range(2,number):
        if all((num % i) !=0 for i in range(2,int(math.sqrt(number))+1)):
           print(num)

number = int(input("Please enter an integer: "))
print_prime_numbers(number)
             
