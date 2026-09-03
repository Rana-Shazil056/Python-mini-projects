names= []
n= int (input("Enter the num of people to strore: "))
for i in range(n):
 while True:
  n=input("Enter the name: ")
  if n.strip()=="":
   print("Name cant be empty!")
  elif not n.isalpha():
   print("name should contain only alphabets! ")
  else:
    names.append(n)
    break

print(names)
print("sorted list is: ",sorted(names))
