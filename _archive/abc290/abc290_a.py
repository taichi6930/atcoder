n, m = map(int, input().split())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
print(sum([A[b - 1] for b in B]))
