a, b, k = map(int, input().split())
x = b - a + 1
for i in range(min(k, x)):
    print(i + a)
c = min(k, x - k)
for j in range(min(k, c)):
    print(b + j - c + 1)
