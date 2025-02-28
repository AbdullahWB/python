with open("newAnotherTwo.txt", "r") as f:
    content = f.read()

with open("newAnother.txt", "r") as f:
    content2 = f.read()
    

if content == content2:
    print("Both files are same")
else:
    print("Both files are different")