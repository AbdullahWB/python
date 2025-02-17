list = ["abdullah", 'd' , 20 , 33.6, True, False, "V5"]
print(list) # ['abdullah', 'd', 20, 33.6, True, False, 'V5']
print(list[0]) # abdullah
print(list[1]) # d
print(list[2]) # 20
print(list[3]) # 33.6
print(list[4]) # True
print(list[5]) # False
print(list[6]) # V5
print(list[-1]) # V5
print(list[-2]) # False
print(list[-3]) # True
print(list[-4]) # 33.6
print(list[-5]) # 20
print(list[-6]) # d
print(list[-7]) # abdullah
print(list[0:2]) # ['abdullah', 'd']
print(list[2:4]) # [20, 33.6]
print(list[4:6]) # [True, False]
print(list[6:7]) # ['V5']
print(list[0:7]) # ['abdullah', 'd', 20, 33.6, True, False, 'V5']
print(list[:7]) # ['abdullah', 'd', 20, 33.6, True, False, 'V5']
print(list[0:7]) # ['abdullah', 'd', 20, 33.6, True, False, 'V5']
print(list[0:7:2]) # ['abdullah', 20, True, 'V5']
print(list[0:7:3]) # ['abdullah', 33.6, 'V5']
print(list[0:7:4]) # ['abdullah', True]
print(list[0:7:5]) # ['abdullah', False]
print(list[0:7:6]) # ['abdullah', 'V5']
print(list[0:7:7]) # ['abdullah']
print(list[0:7:8]) # ['abdullah']
print(list[::]) # ['abdullah', 'd', 20, 33.6, True, False, 'V5']
print(list[::2]) # ['abdullah', 20, True, 'V5']
print(list[::3]) # ['abdullah', 33.6, 'V5']
print(list[::4])

