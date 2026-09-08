########  Reverse of String  #######
def collect_strings():
    str_list = []

    while True:
        s = input("Enter a string (or 'exit' to stop): ")
        if s.lower() == "exit":
            break
        str_list.append(s)

    if str_list:
        print("Strings entered:", str_list)
        # Example: reverse each string
        reversed_list = [x[::-1] for x in str_list]
        print("Reversed strings:", reversed_list)
    else:
        print("No strings entered")

# 👉 Call the function
collect_strings()

####  Count Vowels  ####

def countvowels():
    vowels = "aeiouAEIOU"
    while True:
        count = 0
        s = input("Enter the string or type 'stop' to exit: ")
        if s.lower() == 'stop':
            break
        for character in s:
            if character in vowels:
                count += 1
        print(f"Number of vowels in string is: {count}")
countvowels()
