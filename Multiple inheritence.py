class A :
    def function1(self):
        print("Class A")
class B :
    def Fuction2(self):
        print("Class B")

class C(A,B) :
    def fuction3(self):
        print("Class C")
obj=C()
obj.function1()
obj.Fuction2()
obj.fuction3()