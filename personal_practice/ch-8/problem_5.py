def inc_to_chen(n):
    return n * 2.54

n = int(input("Enter the length in inches: "))

print(f"{n} inches is equal to {round(inc_to_chen(n), 2)} centimeters.")