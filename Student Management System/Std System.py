import json
import os
import time

DATA_FILE = os.path.join(os.path.dirname(__file__), "StudentData_2026.json")


def load_students():
 try:
  with open(DATA_FILE,"r",encoding="utf-8") as File:
   data=json.load(File)
   return data if isinstance(data,list) else [] 
 except (FileNotFoundError,json.JSONDecodeError):
  return


def save_students():
 with open(DATA_FILE, "w", encoding="utf-8") as file:
  json.dump(students, file, indent=4)

students = load_students()


def add_Student():
 print("You Selected 1")
 try:
   roll_no=int(input("Enter the roll number of student: "))
 except ValueError:
   print("Invalid roll number! Please enter a number.")
   return
 for student in students:                               # Student Record check 
  if student["Roll No"]==roll_no:
   print("Student Already Exists!!")
   return
 name=input("Enter the name of student: ")
 try:
   age=int(input("Enter the age of student: "))
 except ValueError:
   print("Invalid age! Please enter a number.")
   return
 Dep=input("Enter the department of student: ")
 students_list={"Roll No":roll_no,"Name":name,"Age":age,"Dep":Dep}
 students.append(students_list)
 save_students()
 print("\nStudent Added Successfully!\n")

def Display():
 if not students:
  print("List is empty! No student record Found!!!")   
 else:
  print(" Student Record\n ")
  for s in students:
    print(f"Roll No : {s['Roll No']} , Name : {s['Name']} , Age : {s['Age']} , Dep: {s['Dep']}")

def Search():
 try:
  roll_no=int(input("Enter the Roll number to search student: "))
 except ValueError:
  print("Enter a valid number!")
  return

 for student in students:
  if student["Roll No"] == roll_no:
   print(f"\nRoll No : {student['Roll No']} , Name : {student['Name']} , Age : {student['Age']} , Dep: {student['Dep']} \n")
   return

 print("No student found with that roll number!")

def Delete():
 try:
  roll_no=int(input("Enter the Roll number to delete student: "))
 except ValueError:
  print("Enter a valid number!")
  return

 for student in students:
  if student["Roll No"] == roll_no:
   print(f"\nRoll No : {student['Roll No']} , Name : {student['Name']} , Age : {student['Age']} , Dep: {student['Dep']} \n")
   students.remove(student)
   save_students()
   print("Student deleted successfully!")
   return

 print("No student found with that roll number!")


def Update():
 try:
  roll_no=int(input("Enter the Roll number to update student: "))
 except ValueError:
  print("Enter a valid number!")
  return

 for student in students:
  if student["Roll No"] == roll_no:
   print("Leave a field blank to keep its current value.")
   name = input(f"Enter the name of student [{student['Name']}]: ")
   age = input(f"Enter the age of student [{student['Age']}]: ")
   department = input(f"Enter the department of student [{student['Dep']}]: ")

   if name:
    student["Name"] = name
   if age:
    try:
     student["Age"] = int(age)
    except ValueError:
     print("Invalid age! Update cancelled.")
     return
   if department:
    student["Dep"] = department

   save_students()
   print("Student updated successfully!")
   return

 print("No student found with that roll number!")

def Count():
 print(f"Total number of students: {len(students)}")

def main():
 while True:
  print("////////////////  Student Management System  ////////////////")
  print("1. Add Student")
  print("2. Display Students")
  print("3. Search Student")
  print("4. Delete Student")
  print("5. Count Students")
  print("6. Update Student")
  print("7. Exit Program")

  try:
   choice=int(input("Enter your choice: "))
  except ValueError:
   print("Enter a valid number!\n")
   continue

  os.system("cls")
  match choice:
   case 1:
    add_Student()
   case 2:
    Display()
   case 3:
    Search()
   case 4:
    Delete()
   case 5:
    Count()
   case 6:
    Update()
   case 7:
    print("Exiting Program....")
    time.sleep(3)
    break
   case _:
    print("OOPS!!! Invalid Input!")

        
if __name__ == "__main__":
    main()