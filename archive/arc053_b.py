import math
import collections


def main():
    S = list(input())
    CS = collections.Counter(S)
    CSValues = list(CS.values())
    A = list(map(lambda x: int(math.copysign(x % 2, x)), CSValues))

    if CSValues.count(1) <= 1:
        print(sum(CSValues))
        return

    print((((sum(CSValues) - CSValues.count(1)) // 2) // CSValues.count(1)) * 2 + 1)


if __name__ == '__main__':
    main()
