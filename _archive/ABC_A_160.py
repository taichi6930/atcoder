def main():
    s = input()
    print('YNeos'[not(s[2] == s[3] and s[4] == s[5])::2])


if __name__ == '__main__':
    main()
