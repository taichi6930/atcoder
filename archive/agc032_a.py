import math
from itertools import accumulate
from copy import deepcopy


def main():
    n = int(input())
    B = list(map(int, input().split()))
    ANS = []

    for i in range(n):
        lenB = len(B)
        for j in range(lenB):
            # 後ろから見ていって、該当する数字があれば
            # ANSに保存して取り除く、出来なければアウト
            if B[lenB - j - 1] == lenB - j:
                ANS.append(lenB - j)
                B.pop(lenB - j - 1)
                break
            if lenB - j - 1 == 0:
                print(-1)
                return
    for j in range(n):
        print(ANS[n - j - 1])


if __name__ == '__main__':
    main()
