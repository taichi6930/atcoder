from collections import Counter


def main():
    n = int(input())
    a, b, c = [None] * n, [None] * n, [None] * n
    for i in range(n):
        x, y = map(int, input().split())
        a[i], b[i], c[i] = x, y, x - y
    ac, bc, cc = Counter(a), Counter(b), Counter(c)
    print("Yes" if max(ac.most_common()[0][1], bc.most_common()
                       [0][1], cc.most_common()[0][1]) >= 3 else "No")


if __name__ == '__main__':
    main()
