def main():
    n, q = map(int, input().split())
    ABList = [[None for _ in range(n + 1)] for _ in range(n + 1)]

    for ab in range(n - 1):
        a, b = map(int, input().split())
        ABList[a][b] = 1

    for cd in range(q):
        c, d = map(int, input().split())


if __name__ == '__main__':
    main()
