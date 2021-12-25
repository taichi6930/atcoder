mod2 = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = [[0] * (max(B) + 1) for _ in range(n + 1)]

    for i in range(2):
        a, b = A[i], B[i]
        for j in range(a, b + 1):
            C[i + 1][j] += 1

    for i in range(1, n):
        a, b = A[i], B[i]
        for q in range(a, b + 1):
            for j in range(q, max(B) + 1):

                C[i + 1][j] = (C[i + 1][j] + C[i][q]) % mod2
    print(sum(C[-1]) % mod2)


if __name__ == '__main__':
    main()
