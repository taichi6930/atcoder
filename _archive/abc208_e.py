def main():
    n, k = map(int, input().split())
    arrayN = list(map(lambda x: int(x), list(str(n))))
    lenN = len(arrayN)

    ans = 0

    if n < 10:
        print(min(k, n))
        return

    # 制限のないところは全部行える（nの桁数以下）
    # 0を含んだ計算
    ans += 10 ** (lenN - 1) - 9 ** (lenN - 1) + min(k, 9) - 1

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(2, len(arrayN)):
        cnt = 0
        B = []
        for j in range(1, 10):
            for a in A:
                q = a * j
                print(q, a, j)
                if q <= k and q % 10 != 0:
                    B.append(q)
                    cnt += 1
        print(B)
        ans += len(B)
        A = B
    print(ans)


if __name__ == '__main__':
    main()
