n, q = map(int, input().split())
lis = []
for _ in range(n):
    lis.append("0")

for _ in range(0, q):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        if lis[i] == "0":
            lis[i] = "1"
        else:
            lis[i] = "0"

print(''.join(lis))
