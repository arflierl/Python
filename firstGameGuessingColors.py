def letsPlay(x):
    if x != "q":
        import random
        print("Welcome to the color guessing game!")
        colors = ["red", "yellow", "aqua", "magenta", "green", "orange"]
        color = colors[random.randint(0, 5)]
        guess = input("guess 'red', 'yellow', 'aqua', 'magenta' 'green', or 'orange: ")
        while guess != color:
            guess = input("Wrong!  Guess again: ")
        else:
            print("That is correct!")
    else:
        print("Okay then, maybe next time! ")
    
    x = input("Press 'Enter' to play again, or type 'q' and hit 'Enter' to quit: ")
    if x == "q":
        print("Thanks for playing, more games coming soon!")
    else:
        letsPlay(x)


letsPlay(input("Press 'Enter' to play color guessing game, or type 'q' to quit: "))

    
