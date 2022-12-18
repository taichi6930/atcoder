n = int(input())
P = [0] + list(map(int, input().split()))

num = n
for i in range(n):
    num = P[num - 1]
    if num == 0:
        exit(print(i))
