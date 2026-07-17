students = dict()

print('''Display Menu

while True:
    try:
        userChoice = int(input("Enter your choice : "))

        if userChoice == 1:
            while True:
                stdId = int(input("Enter your student ID: "))
                stdName = str(input("Enter your Name: "))
                stdAge = int(input("Enter your Age: "))
                stdMarks = int(input("Enter your Marks: "))
                print("Confirm your details")
                print(f'''
                    Student Id : {stdId}
                    Student Name : {stdName}
                    Student Age : {stdAge}
                    Student Marks : {stdMarks}''')
                print('''Press "0" to Confirm''')
                print('''Press "1" to Edit''')
                userConfirm = int(input("Enter your Choice: "))
                if userConfirm == 0:
                    print("Your details are Confirmed")
                    break
            if students["stdId"] == stdId:
                print("You're record is already existed !")
            else:
                print("We found that you're not registered, we are creating your account :)")
                students[stdId] = {
                    "name": stdName,
                    "age": stdAge,
                    "marks": stdMarks
                }
                print("we created your account")
                print(students)
        elif userChoice == 2:
            print(students)
        elif userChoice == 3:
            print("Enter your details to get your record")
            chckId = int(input("Enter your student ID: "))
            chckName = str(input("Enter your Name: "))
            if students.get("stdId")== chckName and students.get("stdName")==chckName:
                print("You're record is already existed !")
                print(f'''(
                
                )''')

    except:
        print("Please enter number from given index !")