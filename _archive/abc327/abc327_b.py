b = int(input())
for a in range(1, 10**9):
    if a**a == b:
        exit(print(a))
    if a**a > b:
        exit(print(-1))
