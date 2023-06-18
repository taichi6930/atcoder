def main():
    s = input()
    l, r = map(int, input().split())
    if len(s) != len(str(int(s))):
        print('No')
        return
    s = int(s)
    if l <= s <= r:
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    main()
