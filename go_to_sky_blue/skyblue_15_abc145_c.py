from itertools import permutations  # 順列全探索で使う


def main():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]
    P = list(permutations([i for i in range(n)]))

    ans = 0

    for p in P:
        for i in range(len(p) - 1):
            ans += ((XY[p[i + 1]][0] - XY[p[i]][0]) ** 2 +
                    (XY[p[i + 1]][1] - XY[p[i]][1]) ** 2) ** 0.5

    print(ans / len(P))


if __name__ == '__main__':
    main()
