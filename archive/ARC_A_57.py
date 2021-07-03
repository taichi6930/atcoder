import sys


def main():
    a, k = map(int, input().split())
    t = a
    cnt = 0

    if k == 0:
        print(2 * 10 ** 12 - a)
        return

    while t < 2 * 10 ** 12:
        cnt += 1
        t += 1 + k * t
    print(cnt)


if __name__ == '__main__':
    main()
