def main():
    n, m = map(int, input().split())
    ABM = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if ABM[a][b] == None:
            ABM[a][b] = c
            continue
        ABM[a][b] = min(ABM[a][b], c)

    ans = 0
    for k in range(1, n + 1):
        for s in range(1, n + 1):
            for t in range(1, n + 1):
                q = k
                if ABM[s][q] != None:
                    if ABM[q][t] != None:
                        if ABM[s][t] != None:
                            ABM[s][t] = min(
                                ABM[s][t], ABM[s][q] + ABM[q][t])
                        else:
                            ABM[s][t] = ABM[s][q] + ABM[q][t]

        for s in range(1, n + 1):
            for t in range(1, n + 1):
                if s == t:
                    continue
                if ABM[s][t] != None:
                    ans += ABM[s][t]
    print(ans)


if __name__ == '__main__':
    main()
