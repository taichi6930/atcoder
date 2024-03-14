x, a, b, c = map(int, input().split())
r = (c * a * b + x * b)
t = a * x
if t == r:
    exit(print('Tie'))
if t < r:
    exit(print('Tortoise'))
print('Hare')
