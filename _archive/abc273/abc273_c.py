from collections import Counter
n = int(input())
A = list(map(int, input().split()))
A2 = sorted(list(set(A)), reverse=True)

lis = Counter(A)

for i in range(n):
    if i >= len(A2):
        print(0)
        continue
    print(lis[A2[i]])
