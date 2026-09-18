#It is an Expenses Management System
import json
import os
from datetime import date
import time

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
 print("Expense Added Sucessfully!!")

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
    return
  print("Searched Id not Found!!!")  

def display():
    if not expenses:
        print("Record is empty! Nothing to Display!!!")
        return

    # Print table header
    print(
        f"\n{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':>10}"
    )
    print("-" * 50)

    # Print each item on a single aligned row
    for expense in expenses:
        e_id = expense.get("ID", "-")
        e_date = expense.get("Date", "-")
        descr = expense.get("Descr", "-")
        amount = expense.get("Amount", 0.0)

        print(f"{e_id:<5} {e_date:<12} {descr:<20} {amount:>10.2f}")


def count():
    if not expenses:
        print("Record is empty! Nothing to calculate.")
        return

    # Display the list first
    display()

    # Calculate total
    totalamount = 0.0
    for expense in expenses:
        totalamount += expense.get("Amount", 0.0)

    # Print summary footer below the table
    print("=" * 50)
    print(f"{'TOTAL AMOUNT':<38} {totalamount:>10.2f}\n")

def delete():
  try:
    id=int(input("Enter the ID of expense u want to delete"))
  except ValueError:
    print("Invalid input!!! plz try again")
    return

  for expense in expenses:
    if id==expense['ID']:
      print(f"ID : {expense['ID']} \nDescription : {expense['Descr']} \nAmount : {expense['Amount']} \nDate : {expense['Date']}")
      expenses.remove(expense)
      save_expenses()
      print("Student removed Successfully")
      return

def main():
 while True:
  print("\n############    Expense Management System   ##############")
  print('''1. Add Expense
2. View All Expenses
3. Search / Filter Expenses
4. Total Expense and summary
5. Delete Expense
6. Exit Program''')
  try:
   n=int(input("\nEnter Your Choice:"))
   
  except ValueError:
   print("Enter valid choice: ")
   continue
  os.system("cls")
  match n:
   case 1:
    add_expense()
   case 2:
    display()
   case 3:
    Search()
   case 4:
    count()
   case 5:
    delete()
   case 6:
    print("Exiting program...")
    time.sleep(3)
    break
   case _:
    print("Invalid choice. Please select a valid option.")

main()