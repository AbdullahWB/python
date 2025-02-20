def print_pattern(n):
    if n == 0:
        return
    
    print("*"*n)
    print_pattern(n - 1)
        
print_pattern(5)