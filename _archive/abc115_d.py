n, x = map(int, input().split())
Y = ['P']

for i in range(n):
    y = Y[-1]
    Y.append('B' + y + 'P' + y + 'B')

print(Y)
