n = int(input("enter NUmber: "))

table = [n*i for i in range(1, 11)]
with open("table.txt", 'w') as f:
    f.write(f"Table of {n}: {str(table)}\n")