class Person:
    def __init__(self):
        self.Person_Name=""
        self.Person_Age=""
        self.Person_Mobile=""
        self.Person_Location=""
        self.Person_Job=""
    def Person_input(self):
        self.Person_Name=input("Enter Person Name")
        self.Person_Age=int(input("Enter Person Age"))
        self.Person_Mobile=int(input("Enter person Mobile Number"))
        self.Person_Location=input("Enter person Location")
        self.Person_Job=input("Enter person Job")
    def display_person(self):
        print("****************")
        print("Name  :",self.Person_Name)
        print("Age  :",self.Person_Age)
        print("Mobile Number   :",self.Person_Mobile)
        print("Location  :",self.Person_Location)
        print("Job  :",self.Person_Job)

class Company:
    def __init__(self):
        self.Company_Name=""
        self.Company_Number=""
        self.Company_Location=""
        self.Company_Email_Id=""
    def Company_input(self):
        self.Company_Name=input('Enter Company Name')
        self.Company_Number=input('Enter Company Contact number')
        self.Company_Location=input('Enter Company Location')
        self.Company_Email_Id=input('Enter Company Email ID')
    def Display_Company(self):
        print("******************")
        print("Compamy Name    :",self.Company_Name)
        print("Compamy Number    :",self.Company_Number)
        print("Compamy Location   :",self.Company_Location)
        print("Compamy Email Id     :",self.Company_Email_Id)

class Employeee(Person,Company):
    def __init__(self):
        self.Skill=""
        self.Salary=""
    def Employee_input(self):
        self.Skill=input("enter Your Skills")
        self.Salary=input("enter Your Salary")
    def Display_employee(self):
        print("***************")
        print("Employeee Skill :",self.Skill)
        print("Employeee Salary :",self.Salary)

obj=Employeee()
obj.Person_input()
obj.Company_input()
obj.Employee_input()
obj.display_person()
obj.Display_Company()
obj.Display_employee()























