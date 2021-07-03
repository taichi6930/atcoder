import sys
import collections
import bisect


def main():
    sk = list(input())
    k = int(input())

    if sk == 1:
        print(0)
        return

    s = sk + sk[0:1]
    changeCnt = 0
    cnt = 1
    while cnt < len(sk) + 1:
        if s[cnt] != s[cnt - 1]:
            cnt += 1
        else:
            if s[cnt + 1] != s[cnt]:
                changeCnt += 1
                s[cnt] = "aaa" + str(cnt)
                cnt += 1
            else:
                changeCnt += 1
                s[cnt] = "aaa" + str(cnt)
                cnt += 2
    print(changeCnt * k)


if __name__ == '__main__':
    main()
