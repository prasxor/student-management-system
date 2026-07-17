students = dict()

print('''Display Menu

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Save to File (Optional)
7. Load from File (Optional)
8. Exit
''')

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
except:
    print("Please enter number from given index !")