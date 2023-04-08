
'''
// A python password geenrator
Written on 7th April, 2023.
'''

import random

print("How long do you want your password to be?")
length = int(input("Choose up to 64 characters: "))

# Making sure the length is equal or less than 64.
if length >64 :
    length = 64
    print("\nSince you wrote a number higher than 64, I'll take the length as 64 by default.")

#creating the  lists.
alphabet = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = ('0123456789')
signs = ('!@#$%^&*')

# Giving the lists a name.
alpha = list(alphabet)
num = list(numbers)
signlist = list(signs)

# Adding the lists together & creating the Password variable.
mainlist = alpha + num + signlist
password = random.choice(mainlist)

# tbh there is probably a better and more efficient way to do this.
while len(password) != length :
    if len(password) != length:
            password =  password + random.choice(mainlist)
            if len(password) == length:
                print(password)
                print("Here you go!")
