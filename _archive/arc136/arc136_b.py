import collections
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = sorted(A)
BB = sorted(B)

if AA != BB:
    print('No')
    exit()

A = collections.deque(A)
B = collections.deque(B)


lenA = len(A)

for i in range(len(A) - 2):
    q = B.index(A[0])
    if q < 3:
        if q == 0:
            A.popleft()
            B.popleft()
        if q == 1:
            B[0], B[1], B[2] = B[1], B[2], B[0]
            A.popleft()
            B.popleft()
        if q == 2:
            B[0], B[1], B[2] = B[2], B[0], B[1]
            A.popleft()
            B.popleft()
        continue
    B[0], B[1], B[q] = B[q], B[0], B[1]
    A.popleft()
    B.popleft()

print('Yes' if A == B else 'No')
