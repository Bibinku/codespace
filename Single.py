class College : #Parent/Base/Main class
    def function1(self):
        print("Inside classs college")
class department(College)  : #child /sub/Deriverd Class
    def Function2(self):
        print("inside class department")
obj = College()
obj.function1()
obj1=department()
obj1.Function2()