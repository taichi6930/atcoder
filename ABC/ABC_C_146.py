import math
import sys
readline = sys.stdin.readline


def main():
    a, b, x = map(int, readline().rstrip().split())
    dn = 0
    n = 0

    for d in range(20):
        dn += 1
        n = int(''.join(str(i) for i in [9] * dn))
        if x <= a * n + b * len(str(n)):
            break
    print(dn)


if __name__ == '__main__':
    main()
