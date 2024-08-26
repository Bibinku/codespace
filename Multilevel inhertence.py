class A:
    def funtion1(self):
        print("inside Class A")
class B(A)  :
    def Fuction2(self):
        print("inside CLASS B")

class C(B)       :
    def Function3(self):
        print("inside Class c")
obj1=C()
obj1.funtion1()
obj1.Fuction2()
obj1.Function3()