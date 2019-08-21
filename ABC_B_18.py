s = list(input())
print(s[1:3])
n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    s[l-1], s[r-1] = s[r-1], s[l-1]
print("".join(s))
