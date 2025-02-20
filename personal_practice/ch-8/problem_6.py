list = ["mohammad", "abdullah", "ali", "akash"]

def remove_words(list, word):
    n = []
    for i in list:
        if not(i == word):
            n.append(i.strip(word))
            
    return n

print(remove_words(list, "a"))