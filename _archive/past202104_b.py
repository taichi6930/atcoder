def main():
    s = list(map(str, input().split('t')))
    if s.count('pos') == 0:
        print('none')
        return
    print(s.index('pos') + 1)


if __name__ == '__main__':
    main()
