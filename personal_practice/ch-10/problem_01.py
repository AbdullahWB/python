class Programmers:
    company = "google"
    def __init__(self, name, salary, age, language):
        self.name = name
        self.salary = salary
        self.age = age
        self.language = language

p = Programmers("John", 1000, 25, "Python")
print(p.name, p.salary, p.age, p.language, p.company)
r = Programmers("Rokib", 1000, 25, "Python")
print(r.name, r.salary, r.age, r.language, r.company)