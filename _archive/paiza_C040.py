n = int(input())
top, bottom = 0, 10000
for _ in range(n):
    a, b = input().split()
    b = float(b)
    if a == 'ge':
        top = max(b, top)
        continue
    if a == 'le':
        bottom = min(b, bottom)
        continue

print(top, bottom)
