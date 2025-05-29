def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

for i in range(1, 101):
    if i % 2 != 0:
        if is_prime(i):
            print(i)