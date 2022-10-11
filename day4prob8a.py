def pw_gen(pw_length):
    import secrets
    import string
    import random
    x = string.ascii_letters + string.punctuation + string.digits
    
    while input("Press enter for new password of type 'q' to quit: ") != 'q':
        pw_length = random.randint(8, 16)
        print(''.join(secrets.choice(x) for i in range(pw_length)))


if __name__ == "__main__" :
    pw_gen(9)
            
        
