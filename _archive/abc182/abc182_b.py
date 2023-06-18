n = int(input())
A = list(map(int, input().split()))
maxA = 0
maxNum = 0
for i in range(2, max(A)+1):
    cnt = 0
    for j in range(n):
        if A[j] % i == 0:
            cnt += 1
    if cnt >= maxA:
        maxA = cnt
        maxNum = i
print(maxNum)
