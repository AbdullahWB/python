def sum_array(n):
    if n == 1:
        return 1
    
    return n + sum_array(n-1)

n = int(input("input the number: "))
print(sum_array(n))


def sumOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    
    return arr[0] + sumOfArray(arr[1:])

arr = [1, 2, 3, 4, 5]
print(sumOfArray(arr))


arr = [1, 2, 3, 4, 5]
print(arr[1:])