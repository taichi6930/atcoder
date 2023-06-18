import collections


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    c = collections.Counter(s)
    print(c.most_common()[0][0])


if __name__ == '__main__':
    main()
