h, w = map(int, input().split())
print(sum([list(input()).count('#') for _ in range(h)]))
