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
# import json
# my_dict={"Class":"9th","Age":9}
# s=json.dumps(my_dict,indent=1)

# with open("Sample.json","w") as f:
#     f.write(s)

# import json

# with open("File_io/Sample.json", "r") as file:
#     data = json.load(file)

# print(data)

import json
# my_dict={"Name":"Shazil","Age":21,"City":"FSD"}
# with open("File_io/Sample.json","w") as file:
#     json.dump(my_dict,file,indent=1)

# json Dump task
# Fav_movies={"2026":"Spider-man",2025:"Iron-man",2005:"Man of Steel"}
# with open("File_io/Sample.json","r") as File:
#     js_str=json.dumps(Fav_movies,indent=4)                    #no File
# print(js_str)

# with open("File_io/Sample.json","w") as File:
#     js_str=json.dump(Fav_movies,File,indent=4)                    #no File
# # print(js_str)


# with open("File_io/Sample.json","r") as f:          # JSON LOAD
#     st=json.load(f)
    
print(st)

