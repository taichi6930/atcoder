def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    B0 = [7 if B[0][i] % 7 == 0 else B[0][i] % 7 for i in range(m)]

    for b in range(len(B0) - 1):
        if B0[b + 1] - B0[b] != 1 or B[0][b + 1] - B0[b + 1] != B[0][b] - B0[b]:
            print('No')
            return

    for a in range(n - 1):
        for b in range(m):
            if B[a + 1][b] - B[a][b] != 7:
                print('No')
                return

    print('Yes')


if __name__ == '__main__':
    main()
