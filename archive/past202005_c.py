import math


def main():
    a, r, n = map(int, input().split())

    if r == 1:
        print(a)
        return

    m = 1 + math.log((10 ** 10) / a, r)
    if n > m:
        print('large')
        return

    ans = a * r ** (n - 1)
    print(ans if ans <= 10 ** 9 else 'large')


if __name__ == '__main__':
    main()
