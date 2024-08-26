class Vehicle:
    def Function(self):



        print(" ")
        print("******VEHICLE DETAILS*****")
        print(" ")


class Car(Vehicle) :
    def __init__(self):
        self.Name=""
        self.colour=""
        self.RC_No=""

    def Carinput(self):
        self.Name=input("Enter Car Name :")
        self.colour=input("Enter Car Colour :")
        self.RC_No=int(input("Enter Car Rc Number :"))
    def DisplayCar(self):



        print("*****CAR DETAILS*****")
        print(" ")
        print("CAR Name   :",self.Name)
        print("CAR Colour   :",self.colour)
        print("CAR RC Number   :",self.RC_No)
        print(" ")
class Bike(Vehicle)   :

    def __init__(self):
        self.Name=""
        self.colour=""
        self.RC_No=""
    def bikeinput(self):
        self.Name=input("Enter Bike Name :")
        self.colour=input("Enter Bike Colour :")
        self.RC_No=int(input("Enter Bike Rc Number :"))
    def Displaybike(self):



        print("*****BIKE DETAILS*****")
        print(" ")
        print("Bike Name   :",self.Name)
        print("Bike Colour   :",self.colour)
        print("Bike RC Number   :",self.RC_No)
        print(" ")

class Bus(Vehicle)    :
    def __init__(self):
        self.Name=""
        self.colour=""
        self.RC_No=""
    def Businput(self):
        self.Name=input("Enter Bus Name :")
        self.colour=input("Enter Bus Colour :")
        self.RC_No=int(input("Enter Bus Rc Number :"))
    def Displaybus(self):


        print("*****BUS DETAILS*****")
        print(" ")
        print("BUS Name   :",self.Name)
        print("BUS Colour   :",self.colour)
        print("BUS RC Number   :",self.RC_No)
        print("")

obj= Car()
obj.Carinput()
obj.Function()
obj.DisplayCar()



obj1=Bike()
obj1.bikeinput()
obj1.Function()
obj1.Displaybike()

obj2=Bus()
obj2.Businput()
obj2.Function()
obj2.Displaybus()

























