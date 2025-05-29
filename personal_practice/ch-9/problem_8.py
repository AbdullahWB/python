with open("newAnother.txt", "r") as f:
    content = f.read()
    
with open("newAnotherTwo.txt", "w") as f:
    f.write(content)