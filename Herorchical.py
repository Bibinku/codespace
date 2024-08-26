class A :
    def parent_function(self):
        
        print("Class A")
class B(A) :
    def fuction1(self):
        print("Class B")
class C(A) :
    def fuction2(self):
        print("Class C")
class D(A)   :
    def fuction3(self):


        print("Class D")



obj=B()
obj.parent_function()
obj.fuction1()


obj1=C()
obj1.parent_function()
obj1.fuction2()

obj2=D()
obj2.parent_function()
obj2.fuction3()
