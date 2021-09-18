def main():
    n, x, m = map(int, input().split())
    aList = [x]
    aNum = -1
    ans = 0

    for i in range(n - 1):
        # 元の値
        An = aList[-1]
        # Anの値
        An1 = An ** 2 % m

        if An1 in aList:
            aNum = aList.index(An1)
            a = An1
            break
        aList.append(An1)
    # まず今まで求めたものを全て足す
    ans += sum(aList)

    if aNum != -1:
        bList = aList[aNum:]
        bListLen = len(bList)

        # 繰り返し足し算するところを求める
        k = (n - len(aList)) // (bListLen)
        ans += sum(bList) * k

        l = n - len(aList) - bListLen * k
        ans += sum(bList[0:l])

    print(ans)


if __name__ == '__main__':
    main()
