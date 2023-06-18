n = int(input())
if n % 5 == 0:
    exit(print(n))
if n % 5 < 3:
    exit(print(n - n % 5))
if n % 5 > 2:
    exit(print(n + 5 - n % 5))
