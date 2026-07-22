students = {}

class Student:
    passing_marks = 35
    student_count = 0
    college_name = "Acme degree college"
    passed_students = []
    failed_students = []

    total_students_view = 0

    def __init__(self,name,age,gender, mobile, email,course,marks):
        self.stdId = "ADC" + str(self.increment_student())
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = self.validate_mobile(mobile)
        self.email = email
        self.course = course
        self.marks = self.is_pass(marks)

        if self.stdId not in students:
            students[self.stdId] = []
        students[self.stdId].append(self)

    @classmethod
    def increment_student(cls):
        cls.total_students_view +=1
        return cls.total_students_view

    @staticmethod
    def validate_mobile(mobile):
        mobile = str(mobile)
        if len(mobile) == 10 and mobile[0] in ['9','8','7','6'] and mobile.isdigit():
            return mobile
        else:
            return "Please enter a valid mobile number"

    @staticmethod
    def display_student(self,curr_inst):
        print(f'''
        student Id   : {curr_inst.stdId}
        student name : {curr_inst.name}
        student age  : {curr_inst.age}
        student gender : {curr_inst.gender}
        student mobile : {curr_inst.mobile}
        student email : {curr_inst.email}
        student course : {curr_inst.course}
        student marks : {curr_inst.marks}
        college name : {curr_inst.college_name}
        ''')

    def is_pass(self,marks):
        if marks >= 35:
            self.passed_students.append(self)
        else:
            self.failed_students.append(self)
        return marks

    # @staticmethod
    def view_student(self):
        for std in students[self]:
            print("---------------------------------------------------")
            print(
                f"customer id : {std.acc_no}\nstd name : {std.c_name}\nstd age : {std.c_age}\nstd bank : {self.bank_name}\nbank manager : {std.manager_name}")
            print("---------------------------------------------------")



# modules

def add_student(std_data):
    # while True:
        print("Confirm your details")
        print(f'''
            Student Id : {std_data[0]}
            Student Name : {std_data[1]}
            Student Age : {std_data[2]}
            Student gender : {std_data[3]}
            Student mobile no. : {std_data[4]}
            Student email : {std_data[5]}
            Student course : {std_data[6]}
            Student Marks : {std_data[7]}
            ''')
        if std_data[0] in students:
            print("You're record is already existed !")
        else:
            print("We found that you're not registered, we are creating your account :)")
            students[std_data[0]] = {
                "name": std_data[1],
                "age": std_data[2],
                "student gender": std_data[3],
                "mobile no": std_data[4],
                "email": std_data[5],
                "course": std_data[6],
                "marks": std_data[7],
            }
            print("we created your account")
            # print(f'''
            #             Student Id : {students[0][0]}
            #             Student Name : {students[0][1]}
            #             Student Age : {students[0][2]}
            #             Student gender : {students[0][3]}
            #             Student mobile no. : {students[0][4]}
            #             Student email : {students[0][5]}
            #             Student course : {students[0][6]}
            #             Student Marks : {students[0][7]}
            #             ''')
            print(students)
            # display_option()

def main_menu():
    print('''
    -------------------------------------------------
    |        Display Menu                           |
    -------------------------------------------------
    | ========= STUDENT RECORD SYSTEM ==============|
    |                                               |      
    |            1. Add Student                     |
    |            2. View All Students               |
    |            3. Search Student                  |
    |            4. Update Student                  |
    |            5. Delete Student                  |
    |            6. Show Passed Students            |
    |            7. Show Failed Students            |
    |            8. Show Topper                     |
    |            9. Average Marks                   |
    |            10. Save Data                      |
    |            11. Load Data                      |
    |            12. Exit                           |
    |-----------------------------------------------|
    ''')



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



def std_input():
    stdId = int(input("Enter your student ID: "))
    try:
        stdName = str(input("Enter your Name: "))
    except:
        print("please enter the valid name !")
    stdAge = int(input("Enter your Age: "))
    stdgender = str(input("Enter your gender: "))
    stdmobile = input("Enter your mobile number: ")
    stdemail = input("Enter your email : ")
    stdCourse = input("Enter your course: ")
    stdMarks = int(input("Enter your Marks: "))


    res :list =[stdId,stdName,stdAge,stdgender,stdmobile,stdemail,stdCourse,stdMarks]
    return res