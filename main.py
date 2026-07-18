from packages.Packages import *
import os

display_option()

while True:
    # try:
        userChoice = int(input("Enter your choice : "))

        if userChoice == 1:

            stdId = int(input("Enter your student ID: "))
            # print("Enter your student Id in INT (Number)")
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
        elif userChoice == 4:
            # try:
            stdId = int(input("Enter your student ID: "))
            # finally:
            # print("Enter your student Id in INT (Number)")
            stdName = str(input("Enter your Name: "))
            stdAge = int(input("Enter your Age: "))
            stdMarks = int(input("Enter your Marks: "))
            update_student(stdId,stdName,stdAge,stdMarks)
        elif userChoice == 5:
            stdId = int(input("Enter your student ID: "))
            print("one record is found")
            print(students[stdId])
            cnf_choice = input("Confirm to delete the record Y[yes] or N[No]: ")
            if cnf_choice == "Y":
                students.pop(stdId)
            elif cnf_choice == "N":
                break
            else:
                print("Please enter Y or N")
        elif userChoice == 6:
            os.chdir(r'/Users/prasxor/Developer/Projects/student-management-system/File Result')
            with open('result.txt','a') as file_result:
                file_result.writelines(str(students[stdId])+"\n")
                print("file saved successfully")
            # print(os.listdir())

    # except:
    #     print("Please enter number from given index !")