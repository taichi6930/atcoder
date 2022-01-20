import collections


def prime_factorization(n):  # 素因数分解を行う
    """
    task:prime factorization
    return:prime
    type:list
    """
    i = 2
    ans = dict()
    k = n
    while i ** 2 <= n:
        while k % i == 0:
            k = k // i
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        i += 1
    if k != 1:
        ans[k] = 1
    return list(ans.items())


def main():
    n = int(input())
    A = list(map(int, input().split()))
    lis = []
    ans = 'setwise coprime'

    for a in A:
        if a == 1:
            continue
        k = list(set(prime_factorization(a)))
        lis += k

    c = collections.Counter(lis)
    d = c.most_common()[0][1]
    if d == n:
        ans = 'not coprime'
    if d == 1:
        ans = 'pairwise coprime'
    print(ans)


if __name__ == '__main__':
    main()
