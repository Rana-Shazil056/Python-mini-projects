def Average():
    
 marks_list=[]
 while True:
   marks_input=input("Enter num (or 'exit' to stop)\n")
   if marks_input.lower()=="exit":
    break
   try:
    marks_list.append(int(marks_input)) 
   except ValueError:
    print("Please enter valid num")
 if marks_list:
  avg=sum(marks_list)/len(marks_list)
 else:
  print("No numbers entered")
 print("List is: ",marks_list)
 print("Average of list is: ",avg)

Average()

def even():
 while True:
   user_input=input("Enter the num to find that num is even or odd and Type 'Quit' to exit ")
   if user_input.lower()=='quit':
    break
   try:
    n=int(user_input)
    if (n%2==0):
      print("Number is EVEN !")
    else:
      print("Number is ODD!")
   except:
    print("Enter valid num")
even()

def largest():
 Numlist=[]
 while True:
  user_input=input("Enter num to input (or type 'Exit' to stop)")
  if user_input.lower()=='exit':
   print("Exiting...")
   break
  else:
   n=int(user_input)
   Numlist.append(n)
 lar=0
 for num in Numlist:
   if lar < num:
    lar = num
   elif lar>num:
    pass
 print("Largest number is ",lar)
 largest()