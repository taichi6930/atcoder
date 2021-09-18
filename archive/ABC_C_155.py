import collections


def main():
    n = int(input())
    S = [input() for _ in range(n)]
    c = collections.Counter(S)
    keys = sorted(c.keys())
    maxS = c.most_common()[0][1]
    for key in keys:
        if c[key] == maxS:
            print(key)


if __name__ == '__main__':
    main()
