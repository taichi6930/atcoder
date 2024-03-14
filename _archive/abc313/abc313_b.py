n, m = map(int, input().split())
B = set(range(1, n + 1))
for _ in range(m):
    _, b = map(int, input().split())
    B.discard(b)

print(B.pop() if len(B) == 1 else -1)
