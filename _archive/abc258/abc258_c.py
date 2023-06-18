n, q = map(int, input().split())
s = list(input())
num = 0
for query in range(q):
    [t, x] = map(int, input().split())
    if t == 1:
        num -= x
    if t == 2:
        print(s[(num + x - 1) % n])
