t, N = map(int, input().split())
s = 1
lis = []
d = 0

for a in range(201):
    b = int(a * (100 + t) / 100)
    if b - a == s:
        if a >= 101:
            d = b - 1 - lis[0]
            break
        lis.append(b - 1)
        s += 1

print(lis[0] + d * ((N - 1) // len(lis)) + lis[(N - 1) % len(lis)] - lis[0])
