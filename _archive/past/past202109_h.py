def main():
    n, x = map(int, input().split())
    ABM = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        if ABM[a][b] == None:
            ABM[a][b] = c
            continue
        ABM[a][b] = min(ABM[a][b], c)

    for k in range(1, n + 1):
        for s in range(1, n):
            for t in range(s + 1, n + 1):
                q = k
                sq1, sq2 = min(s, q), max(s, q)
                tq1, tq2 = min(t, q), max(t, q)
                if ABM[sq1][sq2] != None:
                    if ABM[q][t] != None:
                        if ABM[sq1][sq2] != None:
                            if ABM[s][t] is None:
                                ABM[s][t] = ABM[sq1][sq2] + ABM[tq1][tq2]
                            else:
                                ABM[s][t] = min(
                                    ABM[s][t], ABM[sq1][sq2] + ABM[tq1][tq2])
                        else:
                            ABM[s][t] = ABM[sq1][sq2] + ABM[tq1][tq2]

        for s in range(1, n):
            for t in range(s + 1, n + 1):
                if ABM[s][t] == x:
                    print('Yes')
                    return
    print('No')


if __name__ == '__main__':
    main()
