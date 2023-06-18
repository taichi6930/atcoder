def main():
    n, m = map(int,  input().split())
    aList = sorted(list(map(int,  input().split())), reverse=True)
    aSum = sum(aList)
    mLine = aSum / (4 * m)
    print("Yes" if aList[m - 1] >= mLine else "No")


if __name__ == '__main__':
    main()
