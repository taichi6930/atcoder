from collections import deque


def main():
    n, m = map(int, input().split())
    ansList = [[deque() for _ in range(n)] for _ in range(n)]

    for i in range(m):
        abc = sorted(list(map(int, input().split())))
        [a, b, c] = abc
        setabc = ansList[a - 1][b - 1]
        setabc.append(c)
        ansList[a - 1][b - 1] = setabc
        setabc = ansList[a - 1][c - 1]
        setabc.append(b)
        ansList[a - 1][c - 1] = setabc
        setabc = ansList[b - 1][c - 1]
        setabc.append(a)
        ansList[b - 1][c - 1] = setabc

    ans = 0

    for x in range(n):
        for y in range(n):
            ans = max(ans, len(ansList[x][y]) + len(ansList[y][x]))

    print(ans)


if __name__ == '__main__':
    main()
