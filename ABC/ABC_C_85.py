n, y = map(int, input().split())
swi = 0

for a in range(y//10000 + 1):
    b = (y - 1000 * n - 9000 * a) // 4000
    c = n - a - b
    if 10000 * a + 5000 * b + 1000 * c == y and a >= 0 and b >= 0 and c >= 0:
        print(a, b, c)
        swi = 1
        break
if swi == 0:
    print(-1, -1, -1)
