add_ten = lambda x: x +10
print(add_ten(10))

multiply = lambda x, y: x * y
print(multiply(10, 10))

number = [1, 2, 3, 4, 5, 6, 7, 8]
squared_number = list(map(lambda x: x**2, number))
print(squared_number)

evan_number = list(filter(lambda x: x%2 == 0, number))
print(evan_number)

word = ['apple', 'banana', 'orange']
sorted_word = sorted(word, key=lambda x: len(x))
print(sorted_word)
