a, b, c = map(int, input().split())
if a == b or a == c:
    print((b + c) - a)
else:
    print((a + b) - c)
