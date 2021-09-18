def main():
    n, q = map(int, input().split())
    ANS = [set() for _ in range(n + 1)]

    for i in range(q):
        S = list(map(int, input().split()))
        if S[0] == 1:
            a, b = S[1], S[2]
            ANS[a].add(b)
            continue

        if S[0] == 2:
            a = S[1]
            for i in range(n + 1):
                if a in ANS[i]:
                    ANS[a].add(i)

        if S[0] == 3:
            a = S[1]
            K = list(ANS[a])
            for k in K:
                ANS[a] = ANS[a] | ANS[k]

    ANS = ANS[1::]

    for j in range(n):
        ans = ''
        for z in range(1, n + 1):
            if z - 1 == j:
                ans += 'N'
                continue
            if z in ANS[j]:
                ans += 'Y'
                continue
            ans += 'N'
        print(ans)


if __name__ == '__main__':
    main()
