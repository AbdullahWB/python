class Employee:
    language = "python"
    salary = 10000
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Initialized") # dunder method which call automatically
    
    def display(self):
        print(self.name, self.language, self.salary)
    
    @staticmethod    
    def newLine():
        print("Hello world!")    


Mohammad = Employee("Mohammad", 10000, "javascript")
Mohammad.name = "Mohammad" #instance variable
print(Mohammad.name, Mohammad.salary, Mohammad.language)