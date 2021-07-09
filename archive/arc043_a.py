def main():
    n, a, b = map(int, input().split())
    S = [int(input()) for _ in range(n)]
    deltaS, sumS = max(S) - min(S), sum(S)

    if deltaS == 0:
        print(-1)
        return

    p = b / deltaS
    q = a - b * sumS / deltaS / n
    print(p, q)


if __name__ == '__main__':
    main()
