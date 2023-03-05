from collections import Counter
n, l = map(int, input().split())
A = list(map(int, input().split()))
num = A[0] + 1
cnt = 1

for i in range(1, len(A)):
    k = A[i] + 1
    if num + k > l:
        cnt = i
        break
    num += k

cA = Counter(A[cnt:])

print('Yes' if cA[2] <= (1 if l - num == 2 else 0) else 'No')
