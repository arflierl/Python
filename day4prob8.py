import secrets
import string
import random
import time
def pw_gen(pwlength):
    return ''.join(ramdom.choice(string.ascii_letters +
            string.digits + string.punctuation) for i in range(pwlength))


max_length = 16
print(pw_gen(random.randint(8, max_length)))

