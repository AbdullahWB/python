def max_arr(arr):
    if len(arr) == 1:
        return arr[0]
    
    max_val = max_arr(arr[1:])
    return arr[0] if arr[0] > max_val else max_val

arr = [1, 2, 3, 4, 5]
print(max_arr(arr))
