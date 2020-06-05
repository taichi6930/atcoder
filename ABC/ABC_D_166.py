import math
import sys
readline = sys.stdin.readline


def main():
    x = int(readline().rstrip())
    a, b, c = 0, 0, 1

    while a < 10000:
        c = 1 if a ** 5 - x > 0 else - 1
        b = c * (c * (a ** 5 - x)) ** 0.2
        if b - int(b) == 0:
            print(a, int(b))
            return
        a += 1


if __name__ == '__main__':
    main()
