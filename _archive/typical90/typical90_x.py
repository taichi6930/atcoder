n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(n):
    k -= abs(A[i] - B[i])

print('Yes' if k % 2 == 0 and k >= 0 else 'No')
