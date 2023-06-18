import collections


def main():
    n = int(input())
    R = list(input())

    C = collections.Counter(R)

    print((C["A"] * 4 + C["B"] * 3 + C["C"] * 2 + C["D"]) / n)


if __name__ == '__main__':
    main()
