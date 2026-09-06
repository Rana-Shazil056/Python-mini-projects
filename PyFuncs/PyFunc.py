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

