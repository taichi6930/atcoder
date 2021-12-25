def main():
    n, k = map(int,  input().split())
    nList = [0] * n
    for _ in range(k):
        d = int(input())
        aList = map(int,  input().split())
        for a in aList:
            nList[a - 1] += 1
    print(nList.count(0))


if __name__ == '__main__':
    main()
