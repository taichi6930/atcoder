n = int(input())
a = 2
b = 1
c = 1
if n == 1:
    c = 1
else:
    for i in range(1, n):
        c = b + a
        a = b
        b = c
print(c)
