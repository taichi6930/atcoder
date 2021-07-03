a, b, c = map(int, input().split())
s = "NO"
for i in range(1, b):
    if a * i % b == c:
        s = "YES"
        break
print(s)
