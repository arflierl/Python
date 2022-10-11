def generateTTRows(n: int) -> str:
    v = ["F"] * n 
    print("".join(v))
    i = n-1
    while v != (["T"] * n):
        for j in range (i, 0, -1):
            v[j] = "T"
            print("".join(v))
        for j in range (1, n):
            v[j] = "F"
        v[0] = "T"
        print("".join(v))
        for j in range (1, n):
            v[j] = "T"
            print("".join(v))
