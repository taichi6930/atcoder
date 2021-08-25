def main():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(m - 1):
        for j in range(i + 1, m):
            z = 0
            for k in range(n):
                z += max(A[k][i], A[k][j])
            ans = max(z, ans)
    print(ans)


if __name__ == '__main__':
    main()
