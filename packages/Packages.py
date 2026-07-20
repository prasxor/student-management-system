students = dict()

class Student:
    def __init__(self,std_id,name,age,marks, mobile):
        self.name = name
        self.age = age
        self.marks = marks
        self.stdId = std_id
        self.mobile = self.validate_mobile(mobile)

    course = ["python full stack", "java full stack", "software testing"]
    institute = "qspider"

    @staticmethod
    def validate_mobile(self):
        if len(self.mobile) == 10 and self.mobile[0] in ['9','8','7','6'] and self.mobile.isdigit():
            return self.mobile
        else:
            return "Please enter a valid mobile number"



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

def update_student(stdId,stdName,stdAge,stdMarks):
    if stdId in students:
        students[stdId]["name"] = stdName
        students[stdId]["age"] = stdAge
        students[stdId]["marks"] = stdMarks
        print('Your account details are updated')

def add_student(std_data):
    # while True:
        print("Confirm your details")
        print(f'''
            Student Id : {std_data[0]}
            Student Name : {std_data[1]}
            Student Age : {std_data[2]}
            Student Marks : {std_data[3]}
            Student mobile no. : {std_data[4]}''')
        if std_data[1] in students:
            print("You're record is already existed !")
        else:
            print("We found that you're not registered, we are creating your account :)")
            students[std_data[0]] = {
                "name": std_data[1],
                "age": std_data[2],
                "marks": std_data[3],
                "mobile no": std_data[4]
            }
            print("we created your account")
            print(students)
            # display_option()

def std_input():
    stdId = int(input("Enter your student ID: "))
    try:
        stdName = str(input("Enter your Name: "))
    except:
        print("please enter the valid name !")
    stdAge = int(input("Enter your Age: "))
    stdMarks = int(input("Enter your Marks: "))
    stdmobile = input("Enter your mobile number: ")

    res :list =[stdId,stdName,stdAge,stdMarks,stdmobile]
    return res