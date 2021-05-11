n = int(input())
s = []
t = [[]] * n

for i in range(n):
    s += list(input())

for j in range(len(s)):
    print(j, j % n)
    t[j % n].append(s[j])
print(t)
