def main():
    n, k = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    Alist = [1]
    Blist = []

    ans = 0
    an2 = 0

    for i in range(min(k, 2 * 10 ** 5)):
        # Alistにあった場合
        if A[Alist[i]] in Alist:
            AlistStart = Alist.index(A[Alist[i]])
            Blist = Alist[AlistStart:]
            # print(Alist, Blist)
            # 既にここまでlen(Alist)だけ消化している
            # n - len(Alist)のうち、len(Blist)の倍数は消化される
            q = (k - len(Alist)) % len(Blist)

            # Blistのk番目を取得
            # print(Blist[q])
            return
            # Alistになければappend
        Alist.append(A[Alist[i]])

    print(Alist[-1])


if __name__ == '__main__':
    main()
