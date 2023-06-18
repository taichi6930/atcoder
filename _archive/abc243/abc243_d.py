n, x = map(int, input().split())
s = input()

for i in range(n):
    s = s.replace('RU', '')
    s = s.replace('LU', '')

s = list(s)

k = 0
key = s[0]
sLis = []

for q in s:
    if q == key:
        k += 1
        continue
    sLis.append([key, k])
    key = q
    k = 1

sLis.append([key, k])

print(sLis)

for i in range(len(s)):
    if s[i] == 'U':
        x = x // 2
        continue

    if s[i] == 'L':
        x *= 2
        continue

    if s[i] == 'R':
        x = x * 2 + 1
        continue

print(x)
