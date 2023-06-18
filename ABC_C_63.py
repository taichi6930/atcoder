n = int(input())
x, y = [], []
for i in range(n):
    s = int(input())
    if s % 10 == 0:
        x.append(s)
    else:
        y.append(s)
y = sorted(y)
if len(y) == 0:
    print(0)
elif sum(y) % 10 == 0:
    print(sum(x) + sum(y[1:len(y)]))
else:
    print(sum(x) + sum(y))
