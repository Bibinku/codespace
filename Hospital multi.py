class hospital():
    def __init__(self):
        self.H_name=""
        self.H_Location=""
        self.H_Contact_number =""
    def input_hospital(self):
        self.H_name=input("enter Hospital name")
        self.H_Location=input("enter Hospital Location")
        self.H_Contact_numbere=int(input("enter Hospital contact number"))
    def display_Hospital(self):
        print(" *****HOSPITAL DETAILS***** ")
        print(" Hospital Name   :",self.H_name)
        print(" Hospital Location   :",self.H_Location)
        print(" Hospital Contact number :",self.H_Contact_numbere)

class Department(hospital)   :
    def __init__(self):
        self.D_name=""
        self.D_ID=""
        self.D_HOD=""
    def input_depart(self):
        obj.input_hospital()

        self.D_name=input("enter Department Name")
        self.D_ID=int(input("enter Department ID"))
        self.D_HOD=input("enter Department HOD")
    def display_Depart(self):
        obj.display_Hospital()
        print(" ****** DEPARTMENT DETAILS******")
        print("Department Name     :",self.D_name)
        print("Department ID    :",self.D_ID)
        print("Department HOD    :",self.D_HOD)

class patient(Department):
    def __init__(self):
        self.P_name =""
        self.P_AGE =""
        self.P_Contact =""
        self.P_Doctor =""
    def input_patient(self):
        obj.input_depart()

        self.P_name=input("enter Patient name")
        self.P_Age=input("enter Patient Age")
        self.P_Contact= int(input("enter Patient Contact number"))
        self.P_Doctor=input("enter Patient  Doctor name")
    def display_patient(self):
        obj.display_Depart()
        print("******* PATIENT DETAILS******")
        print("Patient Name   :",self.P_name)
        print("Patient Age   :",self.P_Age)
        print("Patient Contact   :",self.P_Contact)
        print("Patient Doctor Name   :",self.P_Doctor)


obj=patient()
obj.input_patient()
obj.display_patient()
















