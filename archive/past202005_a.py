def main():
    s = input()
    t = input()

    if s == t:
        print('same')
        return

    if s.upper() == t.upper():
        print('case-insensitive')
        return

    print('different')


if __name__ == '__main__':
    main()
