a, b, c = map(int, input().split())
print(max(a, b, c) * (2 ** int(input()) - 1) + (a + b + c))
