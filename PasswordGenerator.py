
'''
// A python password generator.
Written on 7th April, 2023.
'''

import random

print("How long do you want your password to be?")
length = int(input("Choose up to 128 characters: "))

# Making sure the length is equal or less than 128.
if length > 128 :
    length = 128
    print("Since you wrote a number higher than 128, I'll take the length as 128 by default.\n")

alphabet = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = ('0123456789')
signs = ('!@#$%^&*')

# Creating the lists.
alpha = list(alphabet)
num = list(numbers)
signlist = list(signs)

# Adding the lists together & creating the Password variable.
mainlist = alpha + num + signlist
password = random.choice(mainlist)

# tbh there is probably a better and more efficient way to do this.
while len(password) != length :
    password =  password + random.choice(mainlist)
    if len(password) == length:
        print(password)
        print("Here you go!")
