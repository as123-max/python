class Chat:
    contact={'ravi':[],'manu':[],'rajeev':[],'hemand':[]}

    def send_mess(self):
        name=input("enter the name").lower()
        if name in self.contact:
            while True:
                msg=input("enter the message")
                self.contact[name].append(msg)
                n=input("do you want to continue Y or N")
                if n=='N':
                    print("stop conversation")
                    break
        else:
            print("Person not present.")
            m = input("Do you want to add this new person (Y or N)? ").lower()
            if m == 'y':
                self.contact[name] = []  # Add new person to the contact list
                self.send_mess()  
                 
    def dis_msg(self):
        name=input("enter the name").lower()
        if name in self.contact:
            a=len(self.contact[name])
            for i in range(a):
                print(self.contact[name][i],sep='')

class Whatsapp(Chat):
    def __init__(self):
        print("welcome to whatsapp ..chat with your fav ones")

class Instagram(Chat):
    contact={'goutam':[]}
    def __init__(self):
        print("welcome to insta")


    

        
            
    
            
            
    
