def factorial(n):
    if(n==0 or n==1):
        return 1
    
    return n*factorial(n-1) # 4* factorial(3) = 4*3*factorial(2) = 4*3*2*factorial(1) = 4*3*2*1 = 24

print(factorial(4)) # 24