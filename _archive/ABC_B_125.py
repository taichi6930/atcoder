n = int(input())
v, c = [list(map(int, input().split())) for _ in range(2)]
print(sum(v[i] - c[i] for i in range(n) if v[i] > c[i]))
