class Animal:
    name = "Domestic Animal"
    def make_sound(self):
        print(f"Some sound {self.name}")


class Cat(Animal):
    name = "Cat"
    def make_sound(self):
        print(f"Meow Meow {self.name}")
        

class Dog(Animal):
    name = "Dog"
    def make_sound(self):
        print(f"Bark Bark {self.name}")

# Create objects
animal = Animal()
cat = Cat()
dog = Dog()

# Call overridden method
animal.make_sound() # Output: Some sound Domestic Animal
cat.make_sound() # Output: Meow Meow Cat
dog.make_sound() # Output: Bark Bark Dog
print("\n===========\n")
# Accessing parent class attribute
print(animal.name) # Output: Domestic Animal
print(cat.name) # Output: Cat
print(dog.name) # Output: Dog