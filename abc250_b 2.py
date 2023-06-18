n, a, b = map(int, input().split())
lis = ('.' * b + '#' * b) * n
liss = [lis[:(n * b)], lis[b:(n + 1) * b]]

swi = 0
for i in range(n):
    for j in range(a):
        print(liss[swi % 2])
    swi += 1
