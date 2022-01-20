alphaList = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


def main():
    s = list(input())
    t = list(input())
    k = (alphaList.index(t[0]) - alphaList.index(s[0])) % 26

    for i in range(len(s)):
        if alphaList.index(s[i]) + k != alphaList.index(t[i], alphaList.index(s[i])):
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
