def dog_years(age: float) -> float:
    """Given a dogs age in human years, function will calculate
    the dogs age in dog years.

    >>>dog_years(1)
    10.5
    >>>dog_years(9.5)
    51.0
    """
    if age <= 2:
        age = (age * 10.5)
        print(age)
    else:
        age = ((age - 2) * 4) + 21
        print(age)

age = float(input("How old is your dog? "))
dog_years(age)
