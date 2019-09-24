n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = [None] * (m-1)
for i in range(m-1):
    y[i] = x[i+1] - x[i]
print(sum(sorted(y)[0:len(y)-n+1]))
