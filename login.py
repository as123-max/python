class Instagram:
    version=279
    d={}
    def __init__(self):
        n=int(input('enter 1 for login and 2 for signup'))
        if n==1:
            self.Login()
        else:
            self.signup()
                    
    def Login(self):
       print("enter the login details")  
       name=input('enter name')
       if name in self.d:
           while True:
               pw=input("enter pwd")  
               if self.d[name][0]==pw:
                   print("login sucess")
                   break
               else:
                   print("login invalid")
                   k=input("do you want to change password yes or no?")
                   if k=="yes":
                       self.forgetpass(name)
                       break
       else:
            print("the name is not registered please signup")
            self.signup()
    def signup(self):
      print("enter for signup")
      name=input('enter username')
      if  name not in self.d:
          pw=input('enter pwd')
          phno=input('enter no')
          self.d[name]=[pw,phno]
          print("new login")
          self.Login()
    def forgetpass(self,name):
      print("enter details")
      if self.d[name][1]==phno:
          print("you can reset password")
          npwd=input('enter the new pwd')
          rpwd=input('enter reset pwd')
          if npwd==rpwd:
              print("pwd reseted")
              npwd=self.d[name][0]
              self.login()
          else:
              print("the password is not matching")
      else:
          print("enter valid phoneno")
o1=Instagram()
            
        
                

    
              
    
