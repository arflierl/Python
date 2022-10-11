limit = 25
for i in range(1, limit):
    if all((i % 2) ==0 for i in range(2, limit + 1)):
        print(i)

        
