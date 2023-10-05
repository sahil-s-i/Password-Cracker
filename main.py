import os
from random import *
import time

u_pwd = input("Enter a Password : ")
PWD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# If You want add special character in the above list

pw = ""
start_time = time.time()

while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = PWD[randint(0, len(PWD) - 1)]
        pw = str(guess_pwd) + str(pw)
        os.system("cls")
        if pw == u_pwd:
            break
        print(pw)
        print("Cracking Password .... Please Wait !!!")

end_time = time.time()
time_taken = end_time - start_time

print(f"\nYour password is : {pw}")
print(f"\nTime taken to Crack the password: {time_taken:.2f} seconds\n")
