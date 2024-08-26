class college:
    def __init__(self):
        self.College_Name=""
        self.College_Location=""
        self.College_Mobile_No=""
    def Collegedata(self):
        self.College_Name=input("Enter College Name")
        self.College_Location=input("Enter College Location")
        self.College_Mobile_No=int(input("Enter College Mobile number "))
    def DisplayCollege(self):
        print("*******************")

        print("****COLLEGE DETAILS****")
        print("College Name      :",self.College_Name)
        print("College Location      :",self.College_Location)
        print("College  Mobile Number     :",self.College_Mobile_No)

class Department(college):
    def __init__(self):
        self.Dept_Name =""
        self.Dept_Id=""
        self.Dept_Mobile_number=""
    def Departdata(self):
        self.Dept_Name=input("Enter Department Name :")
        self.Dept_Id=int(input("Enter Department ID :"))
        self.Dept_Mobile_number=int(input("Enter Department MOBILE NUMBER:"))
    def DisplayDepart(self):
        print("######################")

        print("####DEPARTMENT DETAILS####")


        print("Department Name         :",self.Dept_Name)
        print("Department ID         :",self.Dept_Id)
        print("Department Mobile Number         :",self.Dept_Mobile_number)
class Student(Department)  :
    def __init__(self):
        self.Student_Name= ""
        self.Student_Age= ""
        self.Student_Mobile_number= ""
        self.Student_Email= ""
        self.Student_Course= ""
        self.Student_LOcation= ""
    def StudentData(self):
        self.Student_Name=input("Enter Student Name ")
        self.Student_Age=int(input("Enter Student Age "))
        self.Student_Mobile_number=int(input("Enter Student Mobile Number  "))
        self.Student_Email=input("Enter Student Email ")
        self.Student_Course=input("Enter Student Course ")
        self.Student_LOcation=input("Enter Student Location ")
    def DisplayStudent(self):
        print("*******************")

        print("****STUDENT DETAILS****")

        print("Student Name      :",self.Student_Name)
        print("Student Age      :",self.Student_Age)
        print("Student Mobile Number       :",self.Student_Mobile_number)
        print("Student Email      :",self.Student_Email)
        print("Student Course      :",self.Student_Course)
        print("Student Location      :",self.Student_LOcation)

obj=Student()
obj.Collegedata()
obj.Departdata()
obj.StudentData()
obj.DisplayCollege()
obj.DisplayDepart()
obj.DisplayStudent()



















