a, b, x = map(int, input().split())
if a % x == 0:
    c = a
else:
    c = (a - a % x)/x
print(c)
