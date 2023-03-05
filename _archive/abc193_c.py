n = int(input())
setA = set()

for a in range(2, int(n ** 0.5) + 1):
    for b in range(2, 10 ** 9):
        k = a ** b
        if k > n:
            break
        setA.add(k)

print(n - len(list(setA)))
