from packages.Packages import *
import os

# from packages.Packages import Student

# display_option()

while True:
    # try:
        main_menu()
        userChoice = int(input("Enter your choice : "))
        if userChoice == 1:
            # std_data = std_input()
            stdname = str(input("Enter your Name: "))
            stdAge = int(input("Enter your Age: "))
            stdgender = str(input("Enter your gender: "))
            stdmobile = input("Enter your mobile number: ")
            stdemail = input("Enter your email : ")
            stdCourse = input("Enter your course: ")
            stdMarks = int(input("Enter your Marks: "))
            student = Student(stdname,stdAge,stdgender,stdmobile,stdemail,stdCourse,stdMarks)
            print(f"student created sucessfully. ID : {student.stdId}")
            # add_student(std_data)
        elif userChoice == 2:
            for student_list in students.values():
                for student in student_list:
                    view_all_students(student)
        elif userChoice == 3:
            print("Enter your details to get your record")
            chckId = input("Enter your student ID: ")
            search_student(chckId.lower())
        elif userChoice == 4:
            print("Enter your details to update your record")
            chckId = input("Enter your student ID: ")
            update_student(chckId.lower())
        elif userChoice == 5:
            print("Enter your details to delete your record")
            chckId = input("Enter your student ID: ")
            delete_student(chckId.lower())
        elif userChoice == 6:
            print(show_passed_students())
        elif userChoice == 7:
            print(show_failed_students())
        elif userChoice == 8:
            print(show_topper())
        elif userChoice == 9:
            os.chdir(r'/Users/prasxor/Developer/Projects/student-management-system/File Result')
            stdId = int(input("Enter your student ID: "))
            if stdId in students:
                with open(f'{students[stdId]}.txt','a') as file_result:
                    file_result.writelines(str(students[stdId])+"\n")
                    print("file saved successfully")
            else:
                print("record not found")
                # print(os.listdir())1
        elif userChoice == 10:
            stdId = int(input("Enter your student ID: "))
            if stdId in students[stdId]:
                with open(f'{students[stdId]}.txt','r') as file_result:
                    file_result.read()
                    print("file saved successfully")
            else:
                print("record not found")
        elif userChoice == 11:
            break
        else:
            print("Enter a valid choice")


    # except:
    #     print("Please enter number from given index !")