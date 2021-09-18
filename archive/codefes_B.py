import collections


def main():
    n = int(input())
    dList = list(map(int,  input().split()))
    m = int(input())
    tList = list(map(int,  input().split()))
    dc = collections.Counter(dList)
    tc = collections.Counter(tList)
    tcKeys = list(tc.keys())
    for tcKey in tcKeys:
        if dc[tcKey] < tc[tcKey]:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
