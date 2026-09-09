import os
students=[]
def add_Student():
 print("You Selected 1")
 name=input("Enter the name of student: ")
 age=int(input("Enter the age of student: "))
 Dep=input("Enter the department of student: ")
 students_list={"Name":name,"Age":age,"Dep":Dep}
 students.append(students_list)
 print("Student Added Successfully!")

def Display():
 if not students:
  print("List is empty! No student record Found!!!")   
 else:
  print(" Student Record\n ")
  for s in students:
   print(f"Name : {s['Name']} , Age : {s['Age']} , Dep: {s['Dep']}")


while True:
 print("////////////////  Student Management System  ////////////////".title())
 n=int(input(("Press 1. for Adding Student: " \
 "\nPress 2. For Display of Students: " \
 "\nPress 3. for Exit program: \n")))
 os.system("cls")
 match n:
    case 1:
     add_Student()
    case 2:
     Display()
    case 3:
     print("Exiting Program....")
    #  os.system("sleep")
     break
    case _:
     print("OOPS!!! Invalid Input!")

        
