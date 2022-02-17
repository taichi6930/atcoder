import collections
mod2 = 998244353


def power_mod(n, k, _mod):
    result = 1
    for i in range(10 ** 20):
        if k <= 0:
            break
        if (k & 1) == 1:
            result = (result * n) % _mod
        n = n * n % _mod
        k >>= 1
    return result


def main():
    x = int(input())
    dic = collections.defaultdict()
    dic[3] = 0
    dic[2] = 0
    dic[x] = 1

    for _ in range(10 ** 10):
        dicKeys = dic.keys()
        maxDic = max(dicKeys)
        if maxDic <= 3:
            break
        dicNum = dic[maxDic]
        a = maxDic // 2
        b = maxDic - a
        if a not in dicKeys:
            dic[a] = 0
        if b not in dicKeys:
            dic[b] = 0

        dic[a] = dic[a] + dicNum
        dic[b] = dic[b] + dicNum
        dic.pop(maxDic)

    print((power_mod(3, dic[3], mod2) * power_mod(2, dic[2], mod2)) % mod2)


if __name__ == '__main__':
    main()
