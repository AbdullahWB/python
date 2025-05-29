for i in range(1, 4):
    line = input("Enter line " + str(i) + ": ")
    with open("test.txt", "a") as file:
        file.write(line + "\n")
print("Lines appended to file")

with open("test.txt", "r") as file:
    print(file.read())