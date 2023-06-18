n = int(input())
A = list(map(int, input().split()))
if n <= 7:
    exit(print(0))
B = [sum(A[:7])]

for i in range(n - 7):
    B.append(B[-1] + A[i + 7] - A[i])

ans = 0
temp_ans = 0

for b in B:
    if b > 5:
        ans = max(ans, temp_ans)
        temp_ans = 0
        continue
    if temp_ans == 0:
        temp_ans = 7
        continue
    temp_ans += 1

print(max(ans, temp_ans))
