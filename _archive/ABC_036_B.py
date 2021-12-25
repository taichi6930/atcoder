n = int(input())
s = [None] * n
for i in range(n):
    s[i] = list(input())

for j in range(n):
    str = [None] * n
    for k in range(n):
        str[k] = s[n - k - 1][j]
    print("".join(str))
