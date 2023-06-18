def main():
    n = int(input())
    aList = list(map(int,  input().split()))
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
