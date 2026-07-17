students = dict()

class Student:
    def __init__(self,stdId,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.stdId = stdId


def display_option():
    print('''
    -------------------------------------------------
    |        Display Menu                           |
    -------------------------------------------------
    |        1. Add Student                         |
    |        2. View All Students                   |
    |        3. Search Student                      |
    |        4. Update Student                      |
    |        5. Delete Student                      |
    |        6. Save to File (Optional)             |
    |        7. Load from File (Optional)           |
    |        8. Exit                                |
    -------------------------------------------------
    ''')

def view_student():
    print(students)

def search_student(stdId):
    if stdId in students:
        print("Your account found")
        print(students[stdId])
    else:
        print("Your account not found")

def add_student(stdId,stdName,stdAge,stdMarks):
    # while True:
        print("Confirm your details")
        print(f'''
            Student Id : {stdId}
            Student Name : {stdName}
            Student Age : {stdAge}
            Student Marks : {stdMarks}''')
        if stdId in students:
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
            display_option()