import collections
mod = 10 ** 9 + 7


def main():
    n = int(input())
    S = list(input())
    ans = 1
    C = collections.Counter(S)
    for val in C.values():
        ans = (ans * (val + 1)) % mod
    print((ans - 1) % mod)


if __name__ == '__main__':
    main()
