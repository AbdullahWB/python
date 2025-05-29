class UserName:
    a = 1
    def showList(self):
         print(f"UserName list no {self.a}")
        
    @property
    def name(self):
        return (f"user first name {self.firstName} and last name is {self.lastName}")
    
    @name.setter
    def name(self, fullName):
        self.firstName, self.lastName = fullName.split()
        

Name = UserName()
Name.name = "Mohammad Abdullah"
print(Name.name)