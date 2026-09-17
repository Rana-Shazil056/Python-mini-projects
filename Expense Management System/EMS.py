#It is an Expenses Management System
import json
import os
from datetime import date

DATA_FILE=os.path.join(os.path.dirname(__file__),"EMS_DATA2026.json")

def load_expense():
 try:
  with open(DATA_FILE,"r",encoding="utf-8") as File:
   data=json.load(File) 
   return data if isinstance(data,list) else []
 except (FileNotFoundError,json.JSONDecodeError):
  return []

def save_expenses():
 with open(DATA_FILE,"w",encoding="utf-8") as file:
  json.dump(expenses,file,indent=4)


expenses=load_expense()

def add_expense():
 try:
  id=int(input("Enter the id for item: "))
 except ValueError:
  print("Invalid input! Try Again")
  return
 for expense in expenses:
  if expense["ID"]==id:
   print("OOPSS!! This id already exists")
   return
descr=input("Enter decription for expense: ")
amount=float(input("Enter the amount for expense: "))
tdate=date.today().strftime("%Y-%m-%d")
expense_data={
  "ID":id,
  "Descr":descr,
  "Amount":amount,
  "Date":tdate
 }
expenses.append(expense_data)
save_expenses()

def Search():
  try:
   d=int(input("Enter the id to search its details: "))
  except ValueError:
   print("Invalid input try again")
   return
  for expense in expenses:

   if d==expense['ID']:
    print("\nExpenses record:\n") 
    print(f"ID : {expense['ID']} \nDescription : {expense['Descr']} \nAmount : {expense['Amount']} \nDate : {expense['Date']}")

  print("Searched Id not Found!!!")  

def display():
 if not expenses:
  print("Record is empty! Nothing to Display!!!")
 else: 
  for expense in expenses:
   print(f"ID : {expense['ID']} \nDescription : {expense['Descr']} \nAmount : {expense['Amount']} \nDate : {expense['Date']}")
  

def main():
 print("############    Expense Management System   ##############")
 print('''1. Add Expense
2. View All Expenses
3. Search / Filter Expenses
4. Delete Expense
5. Summary & Total Spent
6. Filter by Category
7. Exit Program''')
 while True:
  try:
   n=int(input("Enter Your Choice:"))
  except ValueError:
   print("Enter valid choice: ")

match n:
 case 1:
  add_expense()
 case 2:
  display()
 case 3:
     Search()  
main()