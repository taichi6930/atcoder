n = int(input())
A = list(map(int, input().split()))
setA = set(A)

for i in range(2001):
    if i in setA:
        continue
    print(i)
    break
