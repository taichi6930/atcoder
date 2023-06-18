n, m = map(int, input().split())
X = map(int, input().split())
accX = [0] + list(accumulate(X))
CY = [list(map(int, input().split())) for _ in range(m)]
