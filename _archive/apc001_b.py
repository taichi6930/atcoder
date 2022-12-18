n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
k = sum(B) - sum(A)
if k < 0:
    exit(print("No"))

cnt = 0

for i in range(n):
    cnt += max(0, (B[i] - A[i] + 1) // 2)
    if cnt > k:
        exit(print("No"))

exit(print("Yes"))
