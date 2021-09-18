import collections


def main():
    n = int(input())
    P = list(map(int, input().split()))
    Q = []

    a = 0

    for p in P:
        Q.append(p)
        c = collections.Counter(Q)
        for i in range(10 ** 9):
            if c[a] == 0:
                print(a)
                break
            a += 1


if __name__ == '__main__':
    main()
