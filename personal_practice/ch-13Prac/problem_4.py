def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,343,54,34345,656,45,433,454565]
f = list(filter(divisible, a))
print(f)