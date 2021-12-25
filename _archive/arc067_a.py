import math
mod = 10 ** 9 + 7


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n = int(input())
    ansList = []
    k = 1

    for i in range(2, n + 1):
        ans = 0
        # 素数かどうかをチェック
        if not(is_prime(i)):
            continue
        for j in range(1, 20):
            if (i ** j) > n:
                break
            ans += n // (i ** j)
        ansList.append(ans)
    for a in ansList:
        k = (k * (a + 1)) % mod
    print(k)


if __name__ == '__main__':
    main()
