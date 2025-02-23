read = open("test.txt")
# lines = read.readlines()
# print(lines)
# read.close()


while True:
    line = read.readline()
    print(line)
    if line == "":
        break
read.close()