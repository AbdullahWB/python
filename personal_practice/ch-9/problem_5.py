words = ["donkey", "Oh no", "When"]

with open("newFile.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word.lower(), "#"*len(word)).replace(word.capitalize(), "#"*len(word))

with open("newFile.txt", "w") as f:
    f.write(content)