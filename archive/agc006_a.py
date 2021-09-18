import math


def main():
    n = int(input())
    s = list(input())
    t = list(input())
    a = 0
    for i in range(n):
        if "".join(s[n - i - 1:]) == "".join(t[0: i + 1]):
            a = i + 1
    print(2 * n - a)


if __name__ == '__main__':
    main()
