from collections import Counter


def main():
    [n, t] = [int(input()) for _ in range(2)]

    if n >= 3:
        print(10 ** 10 - (n + 1) // 3)
        return
    if n == 1:
        print(10 ** 10 * (t + 1))
        return
    if n == 2:
        print(10 ** 10)
        return


if __name__ == '__main__':
    main()
