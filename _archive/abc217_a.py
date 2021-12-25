def main():
    s1 = list(map(str, input().split()))
    s2 = sorted(s1)

    print('Yes' if s1[0] == s2[0] else 'No')


if __name__ == '__main__':
    main()
