import collections


def main():
    n, k = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(n)]
    P = collections.deque()

    # n = 2
    # ABCD = [[10 ** 6 for _ in range(3)] for _ in range(n)]

    for i in range(n):
        [a, b, c] = ABCD[i]
        d = b + c * (a - 1)
        Q = collections.deque([b + c * j for j in range(a)])
        ABCD[i] = [a, b, c, d]
        P += Q
    # print(sorted(list(P))[k - 1])
    print(ABCD)


if __name__ == '__main__':
    main()
