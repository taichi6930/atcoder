import sys
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    nList = [0] * n
    for _ in range(k):
        d = int(readline().rstrip())
        aList = map(int, readline().rstrip().split())
        for a in aList:
            nList[a - 1] += 1
    print(nList.count(0))


if __name__ == '__main__':
    main()
