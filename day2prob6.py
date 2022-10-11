def check_password(password: str) -> str:
    """function will check that the password meets the following requirments:
    >minimum length of 6 characters
    >maximum length of 16 characters
    >at least 1 letter between [a-z]
    >at least 1 letter between [A-Z]
    >at least 1 number between [0-9]
    >at least 1 character from [$#@]
    
    password = dogs45
    invalid password, password must contain between 6 and 16 characters.

    password = LondonBridge4#
    password ok

    passwrod = waytoomanywordsinthisONE23#2
    invalid password
    """
        
    if len(password) < 6:
        print("invalid password, password must contain between 6 and 16 "
              "characters")
                   
    if len(password) > 16:
        print("invalid password, password must contain between 6 and 16 "
              "characters")

    if not any(c.isupper() for c in password):
        print("invalid password, password must contain at least one"
              " uppercase letter")
    
    if not any(c.islower() for c in password):
        print("invalid password, password must contain at least one"
              " lowercase letter")
        
    if not any(c.isdigit() for c in password):
        print("invalid password, password must contain at least one"
              " number [1-9]")
        
    import re
    valid = True
    if re.search("[S#@]", password):
        print("password ok")
    else:
        print("invalid password, password must contain at least one"
              " of the following characters: '@', '#', or '$'")
    
    
password = str(input("enter pw: "))
check_password(password)

                   

    

    
       
            

    
        
