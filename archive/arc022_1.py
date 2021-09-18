def main():
    ict = list('ict')
    cnt = 0

    S = list(input().lower())

    for s in S:
        if s == ict[cnt]:
            cnt += 1
            if cnt == 3:
                print('YES')
                return
    print('NO')


if __name__ == '__main__':
    main()
