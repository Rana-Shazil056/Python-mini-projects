# with open("D:/Python course CWH/NOTES for python/File_io/Sampletxt.txt", "w") as f:
#     f.write("My name is Shazil")
#     f.close()
# with open("D:/Python course CWH/NOTES for python/File_io/Sampletxt.txt", "r") as f:
#     text=f.read()
#     print(text)


# with open("D:/Python course CWH/NOTES for python/File_io/Sampletxt.txt","r") as f:
#     text=f.readlines()
#     print(text)
# with open("D:/Python course CWH/NOTES for python/File_io/Sampletxt.txt","a") as f:
#     f.write("\nMy marks is 67/100")
# 
#                                            DUMP saves directly to FILE
# import json
# my_dict={"Name":"Shazil","Roll":22}
# with open("Sample.json","w") as file:
#  json.dump(my_dict,file,indent=1)

#                                           DUMPs convert to string later can be saved to file
import json
my_dict={"Class":"9th","Age":9}
s=json.dumps(my_dict,indent=1)

with open("Sample.json","w") as f:
    f.write(s)

