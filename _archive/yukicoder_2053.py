n = int(input())
A = list(map(int, input().split()))

ans = 0
i, j = 0, 1

while i < n:
    k = 0
    while j < n:
        if A[j] - A[i] != j - i:
            break
        k += 1
        j += 1
    i = j
    j += 1
    ans += (k + 1) * k // 2

print(ans)
