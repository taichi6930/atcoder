from itertools import permutations


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]

    # 配列の作成
    P = list(permutations([i for i in range(n)]))

    sumK = 0
    for p in P:
        for a in range(n - 1):
            [x1, y1] = xy[p[a]]
            [x2, y2] = xy[p[a + 1]]
            sumK += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    print(sumK / len(P))


if __name__ == '__main__':
    main()
