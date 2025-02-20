name = input("Enter your name: ")
num = int(input("Enter a number you want to multiply: "))

def multiply(name, num, ending = "Thanks for using this function!"):
    print(f"Hello {name}, your number multiplied by 2 is {num * 2}, {ending}")
    
multiply(name, num, "Goodbye!")