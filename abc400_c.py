N = int(input())

# set型で重複を排除
A = set([])

for a in range(1, N):
    if N < 2**a:
        break
    for b in range(1, N):
        x = 2**a * b**2
        if x > N:
            break
        A.add(x)

print(len(A))
