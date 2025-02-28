with open("newAnother.txt", "r") as f:
    content = f.read()
    
if "python" in content:
   print("python is here")
else:
    print("not here") 