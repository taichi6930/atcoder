import math

s = list(input())
n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    for j in range(math.ceil((r - l + 1)/2)):
        s[l + j - 1], s[r - j - 1] = s[r - j - 1], s[l + j - 1]
print(''.join(s))
