def main():
    alphaList = list("abcdefghijklmnopqrstuvwxyz")
    alphaList2 = list(input())
    n = int(input())
    S1 = [list(input()) for _ in range(n)]

    for i in range(len(S1)):
        for j in range(len(S1[i])):
            S1[i][j] = (alphaList[alphaList2.index(S1[i][j])])
        S1[i] = ''.join(S1[i])
    S1 = sorted(S1)

    for s1 in S1:
        s1 = list(s1)
        for j in range(len(s1)):
            s1[j] = (alphaList2[alphaList.index(s1[j])])
        print(''.join(s1))


if __name__ == '__main__':
    main()
