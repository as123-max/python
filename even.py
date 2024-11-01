'''check = lambda a: a%2==0
print(check(int(input())))'''

'''check = lambda p:p==p[::-1]
print(check(input()))'''

'''check = lambda a: print('mutable') if type(a) in [list,set,dict]else print('not')
print(check(input()))'''

'''class Sample:
    a=10
    b=20
    def __init__(self,name,age):
        self.name=name
        self.age=age
Sample.a=30
ram=Sample('manu',23)
print(Sample.a,Sample.b)
print(ram.name,ram.a,ram.b)'''

class Bank:
    Bank_name='HDFC'
    Bank_loc='BN'
    def __init__(self,name,phno,email):
        self.name=name
        self.phno=phno
        self.email=email

    def info(self):
        print(self.name,self.phno,self.email)
    def uPdate_phno(self,new):
        self.phno=new

yadu=Bank('naran',774571499179,'q@gmail.com')
yadu.info()
        
        
    

