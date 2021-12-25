def main():
    s = list(map(str, input().split('-')))
    print('Yes' if len(s[0]) == 3 and len(s[1]) == 4 else 'No')


if __name__ == '__main__':
    main()
