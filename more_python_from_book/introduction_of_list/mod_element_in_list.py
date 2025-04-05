list = ["abdullah", "mohammad", "afridi", "ali", "siddik"]
list[2]="hello"
print(list[2])
list.append("world")
print(list)
list.insert(0,"gello")
print(list)
del list[0]
print(list)
new_list = list.pop() #for pop specific word use pop(index)
print(list)
print(new_list)
list.insert(0,"world")
print(list.remove("world"))