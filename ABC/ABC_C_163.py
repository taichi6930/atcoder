import sys
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    aList = list(map(int, readline().rstrip().split()))
    aMax = max(aList)
    for i in range(n):
        if aMax >= i + 1:
            print(aList.count(i + 1))
        else:
            print(0)


if __name__ == '__main__':
    main()
