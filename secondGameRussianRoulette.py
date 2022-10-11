def russian_roulette():
    import random
    bullet = random.randint(1, 6)
    guess = int(input("guess which chamber the bullet is in (1-6): "))
    while guess != bullet:
        guess = int(input("guess which chamber the bullet is in (1-6): "))
    else:
        print("Correct! Good thing this isn't real!")

    again = input("To play again, hit 'Enter', or type q and hit enter to quit: ")
    if again == "q":
        print("Thanks for playing, don't play the real thing!")
    else:
        russian_roulette()

        
russian_roulette()
