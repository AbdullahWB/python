# with open("input.txt", "w") as f:
#     cont = """hello world\nthis is a test\ngello world
#     """
#     f.write(cont)
    
    
with open("input.txt", "r") as f:
    cont = f.read()
    print(cont)
    
try:
    with open("output.txt", "w") as f:
        f.write(cont)
except IOError as e:
    print("Error: Cannot open file or write to file", e.message)