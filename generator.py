import string
import random

def generate(length = 6, enableUppercase = True, enableNumber = True, enablePunctuation = True):
    password = ""
    
    #count the required characters.
    count = 0
    if enableUppercase:
        count += 1
    if enableNumber:
        count += 1
    if enablePunctuation:
        count += 1
    

    #prerequiste password component.
    if enableUppercase:
        password = "".join([password, random.choice(string.ascii_uppercase)])
    if enableNumber:
        password = "".join([password, random.choice(string.digits)])
    if enablePunctuation:
        password = "".join([password, random.choice(string.punctuation)])
    
    #generate the rest of the password
    for i in range(length - len(password)):
        rand = random.randint(1, 3)
        if enableUppercase and rand == 1:
            password = "".join([password, random.choice(string.ascii_uppercase)])
        if enableNumber and rand == 2:
            password = "".join([password, random.choice(string.digits)])
        if enablePunctuation and rand == 3:
            password = "".join([password, random.choice(string.punctuation)])
    print("Generated password: " + password)
    return password