a, b, n = [int(input()) for _ in range(3)]
for i in range(1, 20001):
    if (i % a == 0) & (i % b == 0) & (n <= i):
        print(i)
        break
