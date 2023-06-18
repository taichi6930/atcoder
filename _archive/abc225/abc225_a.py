import collections


def main():
    cs = collections.Counter(list(input()))
    print((len(cs) * (len(cs) + 1)) // 2)


if __name__ == '__main__':
    main()
