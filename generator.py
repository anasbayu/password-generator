import string
import random

def generate(length = 6):
    # password must be more than 5 chars.
    if length < 5:
        print('password must be more than 5 characters!')
        return False;
    else:
        password = ""

        password = "".join([password, random.choice(string.ascii_uppercase)])
        password = "".join([password, random.choice(string.digits)])
        password = "".join([password, random.choice(string.punctuation)])

        for i in range(0, length-3):
            rand = random.randint(1, 4)
            if rand == 1:
                password = "".join([password, random.choice(string.ascii_uppercase)])
            if rand == 2:
                password = "".join([password, random.choice(string.digits)])
            if rand == 3:
                password = "".join([password, random.choice(string.punctuation)])
            if rand == 4:
                password = "".join([password, random.choice(string.ascii_lowercase)])

        return password


pwd = generate(10)
print('here is your generated password: ' + pwd)