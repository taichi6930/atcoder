n = int(input())
a, b, c = 2, 1, 1
if n != 1:
    for i in range(1, n):
        a, b, c = b, c, a + b
print(c)
