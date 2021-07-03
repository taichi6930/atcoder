import sys
import math
readline = sys.stdin.readline


def main():
    a, b, h, m = map(int, readline().rstrip().split())
    pi = math.pi
    aArg = (60 * h + m) * pi / 360
    bArg = m * pi / 30
    print(((a * math.cos(aArg) - b * math.cos(bArg)) ** 2 +
           (a * math.sin(aArg) - b * math.sin(bArg)) ** 2) ** 0.5)


if __name__ == '__main__':
    main()
