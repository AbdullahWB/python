string = "welcome to python programming"
list = []

i = 0
while True:
    list.append(string[i])
    i += 2
    if i >= len(string):
        break   
    
print(list)
for i in list:
    print(i, end="")
    
    
    
""" for num in range(10):
    for i in range(num):
        print(num, end="")
    
    print("\n")     """