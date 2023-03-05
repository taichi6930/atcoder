t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(2, n + 1):
        if n % i != 0:
            continue
        r = n // i
        if r % i != 0:
            p = int(r ** 0.5)
            q = i
            print(p, q)
            break
        else:
            q = r // i
            p = i
            print(p, q)
            break
