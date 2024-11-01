class Name:
    def __init__(self,name):
        self.name=name
    def disp(self):
        print(self.name)
class Details:
    def __init__(self):
        print('print remaining details')
class Addr(Name):
    def __init__(self,addr):
        self.addr=addr
class DOB(Addr):
    def __init__(self,dob):
        self.dob=dob
    def disp(self):
        print(self.dob)
class Age(DOB):
    def __init__(self,age):
        self.age=age
    def disp(self):
        print(self.age)
o1=Addr('managlessery')
o2=Name('akash')
o3=Details()
o4=DOB('03-07-2007')
o5=Age('24')
print(o2.name,o1.addr)
print('****')

        

        
