import collections


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    C = collections.Counter(A)
    print(C[x])


if __name__ == '__main__':
    main()
