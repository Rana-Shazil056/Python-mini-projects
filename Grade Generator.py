###########  Grade Generator  #########
def GradeCal():
    subjects = {}
    Grade = ""
    Totalm = 100

    # Input with error handling
    while True:
        try:
            ns = int(input("Enter Num of subjects: "))
            break
        except ValueError:
            print("Enter a valid number!")

    for i in range(ns):
        Sub_n = input("Enter the name of subject: ")
        while True:
            try:
                Sub_marks = int(input(f"Enter the marks for {Sub_n}: "))
                break
            except ValueError:
                print("Marks must be an integer!")
        subjects[Sub_n] = Sub_marks

    TotalMarks = sum(subjects.values())
    TotalPercentage = (TotalMarks / (ns * Totalm)) * 100

    if TotalPercentage >= 90:
        Grade = "A+"
    elif TotalPercentage >= 80:
        Grade = "A"
    elif TotalPercentage >= 70:
        Grade = "B"
    elif TotalPercentage >= 60:
        Grade = "C"
    elif TotalPercentage >= 50:
        Grade = "D"
    else:
        Grade = "F"

    print(f"Your Subjects are: {subjects}")
    print(f"Total Marks: {TotalMarks}/{ns*Totalm}")
    print(f"Percentage: {TotalPercentage:.2f}%")
    print(f"Your Grade is: {Grade}")

GradeCal()
