def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1) 

n = int(input())
print(sum_recursive(n))