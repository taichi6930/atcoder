import collections
n = int(input())
nList = []

for a in range(2, 10**5 + 1):
    for b in range(2, 10**5 + 1):
        if a ** b > n:
            break
        nList.append(a ** b)
print(n - len(list(collections.Counter(nList).keys())))
