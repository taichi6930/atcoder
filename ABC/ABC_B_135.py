n = int(input())
p = list(map(int, input().split()))
q = sorted(p)
num = 0
for i in range(n):
    if p[i] != q[i]:
        num += 1

print("YES" if num == 0 or num == 2 else "NO")
