import collections
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def main():
    n, k = map(int, input().split())
    # グーで勝つ: r, チョキで勝つ: s, パーで勝つ: p
    r, s, p = map(int, input().split())
    rspList = {"r": "p", "s": "r", "p": "s"}
    rspmoneyList = {"r": r, "s": s, "p": p}

    t = list(input())
    myHandList = [None] * n
    ans = 0

    for i in range(n):
        otherhand = t[i]
        myHand = rspList[otherhand]
        if i >= k:
            if myHand == myHandList[i - k]:
                myHandList[i] = 0
                continue
        myHandList[i] = myHand
        ans += rspmoneyList[myHand]

    print(ans)


if __name__ == '__main__':
    main()
