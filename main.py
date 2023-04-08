from PasswordGenerator import *
import os

#Will create a folder
try:
    myfolder = os.mkdir('Password')
except FileExistsError:
    pass

direc = os.getcwd()
# C:\Users\Hany
#"code playgrounds 2.0.txt"
f = open("Folder maker.txt", "a")
f.write(password)

f = open("Folder maker.txt", "r")

os.startfile("password")

#os.open.__format__("Folder maker.txt")
#os.rename("code playgrounds 2.0.txt", "yourpassword.txt")
#os.access("code playgrounds 2.0.txt")