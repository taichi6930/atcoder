def main():
    abclis = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = int(input())
    ans = ''
    for i in range(36 ** 3):
        q = n % 36
        ans += abclis[q]
        n = (n - q) // 36
        if n == 0:
            break
    print(ans[::-1])


if __name__ == '__main__':
    main()
