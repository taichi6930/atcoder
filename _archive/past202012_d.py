def main():
    n = int(input())
    S = [None for _ in range(n)]

    for i in range(n):
        strS = input()
        intS = int(strS)
        zenoS = len(strS) - len(str(intS))
        S[i] = [intS, zenoS, strS]
    S = sorted(sorted(S, key=lambda x: x[1], reverse=True))

    ANS = []
    k = S[0][0]
    an = []

    for j in range(n):
        if S[j][0] == k:
            an.append(S[j])
            continue
        an.sort(key=lambda x: x[1], reverse=True)
        for a in an:
            ANS.append(a[2])
        an = []
        k = S[j][0]
        an.append(S[j])
    an.sort(key=lambda x: x[1], reverse=True)
    for a in an:
        ANS.append(a[2])

    for b in range(n):
        print(ANS[b])


if __name__ == '__main__':
    main()
