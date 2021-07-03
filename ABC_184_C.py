from collections import Counter


def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    print((r1 + c1) - (r2 + c2))
    print((r1 - c1) - (r2 - c2))
    print(abs(r1 - r2) + abs(c1 - c2))


if __name__ == '__main__':
    main()
