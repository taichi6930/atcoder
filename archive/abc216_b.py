import collections


def main():
    n = int(input())
    st = [input() for _ in range(n)]
    C = collections.Counter(st)

    ans = 0

    print('Yes' if max(C.values()) > 1 else 'No')


if __name__ == '__main__':
    main()
