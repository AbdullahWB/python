while True:
    try:
        with open("data.txt", "a") as f:
            title = input("Blog Title: ")
            if title == "0":
                break
            cont = input("Write the contents: ")
            f.write(f"Title: {title}\nContent: {cont}\n\n")
    except FileNotFoundError as e:
        print("Could not found the blog", e.message)
        

with open("data.txt", "r") as f:
    print("\n================================\n")
    print(f.read())