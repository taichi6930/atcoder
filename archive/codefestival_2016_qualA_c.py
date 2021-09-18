alphaList = list("abcdefghijklmnopqrstuvwxyz")

def main():
    s = list(input())
    k = int(input())
    for i in range(len(s) - 1):
        a = (26 - alphaList.index(s[i]))
        if 26 - alphaList.index(s[i]) <= k:
            s[i] = "a"
            k -= a
    s[len(s) - 1] = alphaList[(k + alphaList.index(s[len(s) - 1])) % 26]

    print("".join(s))


if __name__ == '__main__':
    main()
