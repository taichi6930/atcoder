import sys
import math
readline = sys.stdin.readline


def main():
    kArray = []
    for k in range(1, 200):
        kSum = 0
        for a in range(1, k + 1):
            for b in range(1, k + 1):
                for c in range(1, k + 1):
                    kSum += gcd(a, b, c)
        kArray.append(kSum)
        if k % 20 == 0:
            print(kArray)
    print(kArray)


def gcd(a, b, c):
    return math.gcd(math.gcd(a, b), c)


if __name__ == '__main__':
    main()
