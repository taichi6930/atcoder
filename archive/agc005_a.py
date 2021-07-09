import collections
import math
import random
import time

alphaList = list("abcdefghijklmnopqrstuvwxyz")


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    S = ""
    for i in range(200000):
        S += ["S", "T"][random.randrange(2)]
    # S = list(input())
    S = list(S)

    start = time.time()
    cnt = 0
    for i in range(10 ** 9):
        if cnt >= len(S) - 1:
            break
        if "".join(S[cnt: cnt + 2]) == "ST":
            S.pop(cnt + 1)
            S.pop(cnt)
            if cnt == 0:
                continue
            cnt -= 1
            continue
        cnt += 1
    print(len(S))
    finish = time.time()
    print(finish - start)


if __name__ == '__main__':
    main()
