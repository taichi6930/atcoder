n = int(input())
A = sorted(list(map(int, input().split())))
setA = set()

for i, a in enumerate(A):
    for _ in range(10 ** 9):
        if a % 2 != 0:
            setA.add(a)
            break
        a = a // 2

print(len(setA))
