import random

value = random.randint(0, 100)

numbers = list(range(1, 101))

big_list = random.choices(numbers, k=100000)
print(big_list)
