import collections


def main():
    n, k = map(int, input().split())
    S = [input() for _ in range(n)]

    C = collections.Counter(S)
    value = list(C.values())
    C = list(reversed(sorted(list(C.items()), key=lambda x: x[1])))

    if value.count(value[k - 1]) == 1:
        print(C[k - 1][0])
        return
    print('AMBIGUOUS')


if __name__ == '__main__':
    main()
