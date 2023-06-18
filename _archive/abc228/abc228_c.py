def main():
    n, k = map(int, input().split())
    P = [sum(list(map(int, input().split()))) for _ in range(n)]
    q = sorted(P, reverse=True)[k - 1]
    for p in P:
        print('YNeos'[q > (p + 300)::2])


if __name__ == '__main__':
    main()
