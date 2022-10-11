def speeding_points(v: float):
    """ Precondition : v > 0
    """
    if v <= 55:
        print("Ok")
    if 55 < v < 115:
        print("Points: ", (v-55)//5)
    if v >= 115:
        print("License suspended")

v = float(input("Enter drivers speed in mph or type '0' to quit: "))
while v != 0:
    speeding_points(v)
    v = float(input("Enter drivers speed in mph or type '0' to quit: "))
print("exiting program, have a good day. ")
    

            
      
