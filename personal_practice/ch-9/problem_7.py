with open("newAnother.txt") as f:
    content = f.readlines()

lineNo = 1
for line in content:
    if "python" in line.lower():
        print(f"Line {lineNo}: Python is here")
        break
    lineNo += 1
else:
    print("Python is not here")