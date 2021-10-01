def main():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))
    P = list(map(int, input().split()))

    A = {}

    for i in range(n):
        c, p = C[i], P[i]
        if c not in A:
            A[c] = p
            continue
        A[c] = min(A[c], p)

    Avalues = sorted(list(A.values()))
    if len(Avalues) < k:
        print(-1)
        return
    print(sum(Avalues[:k]))


if __name__ == '__main__':
    main()
