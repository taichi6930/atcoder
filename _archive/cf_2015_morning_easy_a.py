n = int(input())
for i in range(10001):
    if i ** 2 >= n:
        exit(print(i ** 2 - n))
