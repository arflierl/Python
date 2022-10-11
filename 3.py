def summer_winter(x) :
 """Funtion will retun Summer if given number
    is divisible by 3, Winter if divisible by
    5, and SummerWinter if divisible by both.
    If given number is divisible by neither
    3 or 5, funcion will return given number.
 >>>summer_winter(9)
    Summer
 >>>summer_winter(25)
    Winter
 >>>summer_winter(30)
    SummerWinter
 >>>summer_winter(2)
    2.0
 """
 if x % 3 == 0 and x % 5 != 0:
        print("Summer")
 if x % 3 != 0 and x % 5 == 0:
        print("Winter")
 if x % 3 == 0 and x % 5 == 0:
        print("SummerWinter")
 if x % 3 != 0 and x % 5 != 0:
        print(x)
x = float(input("Please enter a number: "))
summer_winter(x)




