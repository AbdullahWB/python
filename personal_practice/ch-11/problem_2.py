class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof Woof")
        
        
D = Dog()
D.bark()