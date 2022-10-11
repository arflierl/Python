def is_longer(L1: list, L2: list) -> bool:
    if len(L1) > len(L2):
        print("True")
    else:
        print("false")

L1 = [1, 3, 4, 7]
L2 = [3, 4, 6, 8, 6, 2, 1]
is_longer(L1, L2)
