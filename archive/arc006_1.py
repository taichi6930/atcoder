def main():
    E = list(map(int, input().split()))
    B = int(input())
    L = list(map(int, input().split()))
    cnt = 0

    for l in L:
        if l in E:
            cnt += 1

    if cnt == 6:
        print(1)
        return
    if cnt == 5:
        if B in L:
            print(2)
            return
        print(3)
        return
    if cnt == 4:
        print(4)
        return
    if cnt == 3:
        print(5)
        return
    print(0)


if __name__ == '__main__':
    main()
