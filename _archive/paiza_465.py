n, m = map(int, input().split())
A = [int(input()) for _ in range(m)]

ans = 0

for _ in range(n):
    H = [int(input()) for _ in range(m)]
    temp_ans = 100
    for i in range(m):
        dx = abs(A[i] - H[i])
        if dx <= 5:
            continue
        if dx <= 10:
            temp_ans -= 1
            continue
        if dx <= 20:
            temp_ans -= 2
            continue
        if dx <= 30:
            temp_ans -= 3
            continue
        temp_ans -= 5
    ans = max(temp_ans, ans)

print(ans)
