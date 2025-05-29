a = 69

def fun():
    global a
    a = 96
    return a

fun = fun()
print(a) 