class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"hello, my name is {self.name} and i am {self.age} year old"

person1 = Person("Abdullah", 21)
person2 = Person("Mohammad", 25)

print(person1.greet())
print(person2.greet())