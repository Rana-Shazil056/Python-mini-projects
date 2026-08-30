############## TABLE GENERATOR ##########
# 
#  This program generates a multiplication table for a given number.

import os
while True:
 y=input("Enter Y to continue or E to exit: ")
 match y.upper():
  case "Y":
   os.system("cls")
   while True:
    try:
        n=int(input("Enter the number for which you want multiplication Table: "))
        for i in range(1,11):
                 print(f"{n} x {i} = {n*i}")
        break
    except ValueError:
       print("Invalid input!!! Try again by inputting integer") 
  case "E":
       print("Exiting!!!")
       break
  case _:
       print("Invalid input! Try Again")