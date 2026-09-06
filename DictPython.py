fields=['name','age','marks']
n= int(input("Enter the num of students: "))
students=[]       #list where dictionaries will be stored
for i in range(1,n+1):
    student_data={}     #dictionary
    for field in fields:
        std_input=input(f"For student {i} Enter {field}: ")
        student_data[field]=std_input
    students.append(student_data)

print("$$$$$ Student Record $$$$$$")
for s in students:            # Diplay
 print(s)



