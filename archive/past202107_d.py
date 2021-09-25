def main():
    n = int(input())
    s = list(input())
    lis = ['axa', 'ixi', 'uxu', 'exe', 'oxo']

    for i in range(n):
        if i + 3 > n:
            break
        if ''.join(s[i: i + 3]) in lis:
            for j in range(3):
                s[j + i] = '.'
    print(''.join(s))


if __name__ == '__main__':
    main()
