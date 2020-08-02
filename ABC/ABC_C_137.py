import collections


def main():
    n = int(input())
    cSum = 0
    for cVal in collections.Counter(
            [''.join(sorted(list(input()))) for _ in range(n)]).values():
        cSum += cVal * (cVal - 1) // 2
    print(cSum)


if __name__ == '__main__':
    main()
