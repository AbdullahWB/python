class Employee:
    language = "python"
    salary = 10000
    
    def display(self):
        print(self.name, self.language, self.salary)
    
    @staticmethod    
    def newLine():
        print("Hello world!")    


Mohammad = Employee()
Mohammad.name = "Mohammad" #instance variable
Mohammad.language = "Java" #instance variable
Mohammad.salary = 120000 #instance variable
print(Mohammad.name, Mohammad.language, Mohammad.salary)

Abdullah = Employee()
Abdullah.name = "Abdullah" #instance variable
Abdullah.language = "C/C++" #instance variable
Abdullah.salary = 150000 #instance variable
print(Abdullah.name, Abdullah.language, Abdullah.salary)


Mohammad.display() #method call to display Mohammad's details # and this pass one argument
Employee.display(Mohammad) #method call like dis func call to display

Abdullah.newLine() #method call to print a new line