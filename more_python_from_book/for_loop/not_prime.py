miss = 0
notMiss = 0
for i in range(1, 100):
    if i % 2 != 0:
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print("not miss", i)
            notMiss+=1
        else:
            print("miss", i)
            miss+=1

print(miss, notMiss)
            