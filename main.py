import os
from random import *

u_pwd = input("Enter a Password : ")
PWD = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9']

pw = ""

while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = PWD[randint(0, len(PWD) - 1)]
        pw = str(guess_pwd) + str(pw)
        os.system("cls")
        print(pw)
        print("Cracking Password .... Please Wait !!!")

print(f"\nYour password is : {pw}")

# ! LET'S CRACK IT
