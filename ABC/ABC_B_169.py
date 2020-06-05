import math
import sys
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    aList = list(map(int, readline().rstrip().split()))
    ans = 1

    if 0 in aList:
        print(0)
        return

    for a in aList:
        ans *= a
        if ans > 10 ** 18:
            ans = -1
            break
    print(ans)


if __name__ == '__main__':
    main()
