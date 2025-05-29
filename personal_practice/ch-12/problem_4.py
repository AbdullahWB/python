try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    