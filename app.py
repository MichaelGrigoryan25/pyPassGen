#Import libraries
import time
import string
from random import *

#Dots loader
def dotLoader():
    for x in range (0,5):  
        b = "Starting" + "." * x
        print (b, end="\r")
        time.sleep(0.8)

#Bracket loader
def bracksLoader():
    print("Starting to generate a secure password")
    for x in range (2):  
        a = "[|]"
        b = "[/]"
        c = "[-]"
        d = "[\]"
        print (a, end="\r")
        time.sleep(0.5)
        print (b, end="\r")
        time.sleep(0.5)
        print (c, end="\r")
        time.sleep(0.5)
        print (d, end="\r")
        time.sleep(0.5)

#Password Generator
def passGen():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(16, 16))) #Will generate a 16 character password
    print(password)

#Welcome "screen"
def welcome():
    print("Welcome To Python Password Generator!")
    print("-------------------------------------")
    a = input("Do you want to proceed? [y/n]: ")
    if a == "y":
        bracksLoader()
        passGen()
    else:
        exit()

#Execute defined functions
dotLoader()
welcome()