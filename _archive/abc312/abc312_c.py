n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

print(A, B)
