n, p, q = map(int, input().split())
print(min(p, q + min(list(map(int, input().split())))))
