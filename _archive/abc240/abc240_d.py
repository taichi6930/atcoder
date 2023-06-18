import random


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    last = None
    cnt = 0
    lenB = 0

    lastList = []
    cntList = []

    for i in range(len(A)):
        a = A[i]
        # 一番後ろの球が同じ数字だった場合
        if last == a:
            # cntを1足し、Bに追加し、lenBを1足してあげる
            cnt += 1
            B.append(a)
            lenB += 1
            # もしcntがaと同じ数字だった場合、爆破する
            if cnt == a:
                lenB = sum(cntList)

                # lastの数字とcntを計算してあげる
                if lenB == 0:
                    last = None
                    cnt = 0
                else:
                    last = lastList.pop()
                    cnt = cntList.pop()

        # 一番後ろの球が同じ数字だった場合 lastをその数字に変え、cntを1に、Bに追加し、lenBを1足し、出力
        else:
            lastList.append(last)
            last = a
            cntList.append(cnt)
            cnt = 1
            lenB += 1
        print(lenB)


if __name__ == '__main__':
    main()
