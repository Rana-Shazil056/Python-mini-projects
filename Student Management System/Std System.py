import os
students=[]
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
   print("Student deleted successfully!")
   return

 print("No student found with that roll number!")

def main():
 while True:
  print("////////////////  Student Management System  ////////////////")
  print("1. Add Student")
  print("2. Display Students")
  print("3. Search Student")
  print("4. Delete Student")
  print("5. Exit Program")

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
    print("Exiting Program....")
    break
   case _:
    print("OOPS!!! Invalid Input!")

if __name__ == "__main__":
 main()

        
