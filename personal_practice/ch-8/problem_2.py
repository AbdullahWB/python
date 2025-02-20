f = int(input("Enter the temperature in Fahrenheit: "))

def f_to_c(f):
    c = 5*(f - 32)/9
    return c

c = f_to_c(f)

print(f"{f} degrees Fahrenheit is equal to {round(c,2)} degrees Celsius.")