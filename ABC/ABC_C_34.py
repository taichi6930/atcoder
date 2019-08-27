w, h = map(int, input().split())
a = 1
b = 1
for i in range(0, h - 1):
    a *= w + h - 2 - i
    b *= h - i

print(int(a/b) % 1000000007)
