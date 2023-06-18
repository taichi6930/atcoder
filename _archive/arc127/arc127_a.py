n = int(input())

ans = 0

for i in range(17):
    if int("1" * i) > n:
        break
