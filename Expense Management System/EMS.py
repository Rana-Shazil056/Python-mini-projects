#It is an Expenses Management System
import json
import os
import time

DATA_FILE=os.path.join(os.path.dirname(__file__),"EMS_DATA2026.json")

def load_expense():
 try:
  with open(DATA_FILE,"r",encoding="utf-8") as File:
   data=json.load(File) 
   return data if isinstance(list,data) else []
 except (FileNotFoundError,json.JSONDecodeError)
 return 

def save_expenses():
 with open(DATA_FILE,"w",encoding="utf-8") as file:
  json.dump(expenses,file,indent=4)


expenses=load_expense()







def main():
 print("############    Expense Management System   ##############")
 print('''1. Add Expense
2. View All Expenses
3. Search / Filter Expenses
4. Delete Expense
5. Summary & Total Spent
6. Filter by Category
7. Exit Program''')
# while True:
#  try:
#   n=int(input("Enter Your Choice:"))
#  except ValueError:
#   print("Enter valid choice: ")

#   match n:
#    case 1:
#     add_expense()
# main()