class Employee:
    company = "MAT"
    def show(self):
        print(f"The name of the employee in your company {self.name} is work on {self.company} this company")
        

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language of the coder is {self.language}")


class Programmer(Employee, Coder):
    name = "John"
    company = "MAT ite"
    def printDetails(self):
        print(f"The name of the programmer is {self.name} nad company name is {self.company} and language is {self.language}")
        self.show()
        self.printLanguage()
        
p = Programmer()

p.printDetails()
p.printLanguage()
p.show()
