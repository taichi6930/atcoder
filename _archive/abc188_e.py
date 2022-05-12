n, m = map(int, input().split())
A = list(map(int, input().split()))
XY = sorted([list(map(int, input().split()))
            for _ in range(m)], key=lambda x: (x[1], x[0]))
goldList = [1] + [0] * (n - 1)
silverList = [0] * n

print(silverList)
