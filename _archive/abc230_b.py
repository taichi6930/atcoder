def main():
    s = input().split('o')
    t = s[1: -1]
    print('Yes' if t.count('xx') == len(t) and len(
        s[0]) < 3 and len(s[-1]) < 3 else 'No')


if __name__ == '__main__':
    main()
