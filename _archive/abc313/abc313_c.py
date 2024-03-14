from statistics import mean as avg

n = int(input())
A = sorted(list(map(int, input().split())))
avgA = int(avg(A))

B = [avgA for _ in range(n * (1 + avgA) - sum(A))] + [
    avgA + 1 for _ in range(sum(A) - n * avgA)
]

print(sum([abs(a - b) for a, b in zip(A, B)]) // 2)
