a = int(input("number first: "))
b = int(input("number second: "))

if a == 0 or b == 0:
    raise ZeroDivisionError("Number must be a positive number or negative number not zero.")
else:
    print(f"The sum of {a} and {b} is: {a / b}")