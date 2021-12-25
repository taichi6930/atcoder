from math import copysign


def main():
    n = int(input())
    A = sorted(list(map(int, input().split())))
    ans = sum(list(map(lambda x: int(copysign(x ** 2, x)), A)))
    print(n, A, ans)


if __name__ == '__main__':
    main()
