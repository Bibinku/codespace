class college:
    def __init__(self):
        self.C_Name = ""
        self.Location =""
        self.Mobile_number =""
    def College_date(self):
        self.C_Name=input("enter college name")
        self.Location=input("enter Location name")
        self.Mobile_number=int(input("enter Mobile  number "))
    def Display_data(self):
        print("#######################")
        print("College Name      :",self.C_Name)
        print("College Location     :",self.Location)
        print("College Mobile N0    :",self.Mobile_number)
class Department(college)  :
    def __init__(self):
        self.Department_Id=""
        self.Department_Name=""
        self.Mobile_n0=""
    def Dept_Data(self):
        self.Department_Id=input("Enter College department ID")
        self.Department_Name=input("Enter College department Name")
        self.Mobile_n0=int(input("Enter College Mobile No"))
    def display_dept(self):

        print("########################")
        print("Department ID      :",self.Department_Id)
        print("Department Name     :",self.Department_Name)
        print("Department Mobile No      :",self.Mobile_n0)

obj=Department()
obj.College_date()
obj.Dept_Data()

obj.Display_data()
obj.display_dept()


