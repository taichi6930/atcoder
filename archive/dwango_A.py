def main():
    n = int(input())
    stList = [list(map(str,  input().split())) for _ in range(n)]
    x = input()
    sumT = 0
    flg = False

    for i in range(n):
        s, t = stList[i][0], int(stList[i][1])
        if flg == False:
            if s == x:
                flg = True
                continue
        sumT += t
    print(sumT)


if __name__ == '__main__':
    main()
