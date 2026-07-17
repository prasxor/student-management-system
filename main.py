from Packages import *



display_option()

while True:
    # try:
        userChoice = int(input("Enter your choice : "))

        if userChoice == 1:
            try:
                stdId = int(input("Enter your student ID: "))
            finally:
                print("Enter your student Id in INT (Number)")
            stdName = str(input("Enter your Name: "))
            stdAge = int(input("Enter your Age: "))
            stdMarks = int(input("Enter your Marks: "))
            add_student(stdId,stdName,stdAge,stdMarks)
        elif userChoice == 2:
            view_student()
        elif userChoice == 3:
            print("Enter your details to get your record")
            chckId = int(input("Enter your student ID: "))
            search_student(chckId)

    # except:
    #     print("Please enter number from given index !")