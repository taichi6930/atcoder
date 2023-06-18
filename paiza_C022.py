st, gl, top, bottom = 0, 0, 0, 0

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if i == 0:
        st = a
        bottom = d
    if i == n - 1:
        gl = b
    top = max(top, c)
    bottom = min(bottom, d)

print(st, gl, top, bottom)
