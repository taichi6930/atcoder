n, k = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(n)])
sumB = sum([AB[i][1] for i in range(n)])
if sumB <= k:
    print(1)
    exit()
for i, [a, b] in enumerate(AB):
    sumB -= b
    if sumB <= k:
        print(a + 1)
        break
