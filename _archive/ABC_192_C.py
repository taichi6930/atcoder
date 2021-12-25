n, k = map(int, input().split())
n = str(n)
for i in range(k):
    na = int("".join(sorted(n, reverse=True)))
    nb = int("".join(sorted(n)))
    n = str(na - nb)
print("".join(n))
