"""Problem 4:  Write and test a function that asks for the names of all the
memebers in a club.  However, we don't know how many members there actually
are.  We will use a "while-loop" which will repeat until all the members
names have been entered.  The user will be able to print a list of all
members and exit the program by entering "q"
"""

def club_members():
    members = []
    
    
    name = str("")
    while name != str("q"):
        name = str(input("Please enter club members name or type 'q' to print " +
        "list of members and quit: "))
        if name != "q":
            members.append(name)
    for name in range(len(members)):
        print(members[name])
    print("Exiting program....")




    
