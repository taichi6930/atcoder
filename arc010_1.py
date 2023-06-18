def main():
    n, m, a, b = map(int, input().split())
    cnt = n * 1

    for i in range(m):
        if cnt <= a:
            cnt += b
        c = int(input())
        cnt -= c

        if cnt < 0:
            print(i + 1)
            return
    print('complete')


if __name__ == '__main__':
    main()
