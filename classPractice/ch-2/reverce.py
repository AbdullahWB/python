def reverse(s):
    reverseStr = ""
    for char in s:
        reverseStr = char + reverseStr
    return reverseStr

print(reverse("hello"))