import collections


def main():
    n, l = map(int, input().split())
    ANS = collections.deque([0] + [None for _ in range(l)])
    Hardle = collections.deque([0 for _ in range(l + 1)])
    X = list(map(int, input().split()))
    T1, T2, T3 = map(int, input().split())

    for a in range(n):
        Hardle[X[a]] = 1

    for i in range(1, l + 1):
        minANS = None

        # # その場所にハードルがあったら引っかかるということで計算する
        # t4 = T3 if Hardle[i] == 1 else 0

        # 行動1が最適である時
        if ANS[i - 1] is not None:
            # その場所にハードルがあったら引っかかるということで計算する
            ta = T3 if Hardle[i - 1] == 1 else 0
            if minANS is None:
                minANS = T1 + ta + ANS[i - 1]
            else:
                minANS = min(minANS, T1 + ta + ANS[i - 1])

        # # 行動2が最適である時
        if i >= 2:
            if ANS[i - 2] is not None:
                # その場所にハードルがあったら引っかかるということで計算する
                ta = T3 if Hardle[i - 2] == 1 else 0
                if minANS is None:
                    minANS = (ta + T1 + T2) + ANS[i - 2]
                else:
                    minANS = min(minANS, (ta + T1 + T2) + ANS[i - 2])

        # 行動3が最適である時
        if i >= 4:
            if ANS[i - 4] is not None:
                # その場所にハードルがあったら引っかかるということで計算する
                ta = T3 if Hardle[i - 4] == 1 else 0
                if minANS is None:
                    minANS = (ta + T1 + 3 * T2) + ANS[i - 4]
                else:
                    minANS = min(minANS, (ta + T1 + 3 * T2) + ANS[i - 4])
        ANS[i] = minANS
    print(ANS[-1])


if __name__ == '__main__':
    main()
