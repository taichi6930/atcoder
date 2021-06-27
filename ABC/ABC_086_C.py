n = int(input())
x1, y1, t1 = 0, 0, 0
ans = "Yes"

for i in range(n):
    t2, x2, y2 = map(int, input().split())
    if (t2 - t1) < (abs(x2 - x1) + abs(y2 - y1)) or (t2 - t1) % 2 != (abs(x2 - x1) + abs(y2 - y1)) % 2:
        ans = "No"
    t1, x1, y1 = t2, x2, y2

print(ans)
