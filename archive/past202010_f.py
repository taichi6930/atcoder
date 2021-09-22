import collections


def main():
    n, k = map(int, input().split())
    S = [input() for _ in range(n)]
    C = collections.Counter(S)
    x = sorted(list(C.values()), reverse=True)[k - 1]
    if list(C.values()).count(x) > 1:
        print('AMBIGUOUS')
        return
    print(list(C.keys())[list(C.values()).index(x)])


if __name__ == '__main__':
    main()
