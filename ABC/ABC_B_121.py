N, M, C = map(int, input().split())
B = list(map(int, input().split()))
cnt = 0

for n in range(N):
    sum = C
    A = list(map(int, input().split()))
    for m in range(M):
        sum += A[m]*B[m]
    if sum > 0:
        cnt += 1

print(cnt)
