import collections


def main():
    q, h, s, d = map(int, input().split())
    n = int(input())
    cnt = 0

    qhsd = [d, s * 2, h * 4, q * 8]

    # 2Lを買う
    if n // 2 >= 1:
        cnt += min(qhsd[0:]) * 2 ** qhsd.index(min(qhsd[0:]))
    #     n -= n // 2
    #     print(cnt)
    #     print(n)
    # # 1Lを買う
    # if n // 1 >= 1:
    #     cnt += min(qhsd[1:]) * qhsd.index(qhsd[1:]) // 2
    #     n -= n // 1

    # # 0.5Lを買う
    # if n * 2 >= 1:
    #     cnt += min(qhsd[2:]) * qhsd.index(qhsd[2:]) // 4
    #     n -= n * 2

    # # 0.25Lを買う
    # if n * 4 >= 1:
    #     cnt += min(qhsd[3:]) * qhsd.index(qhsd[3:]) // 8
    #     n -= n * 4

    print(n)
    print(cnt)


if __name__ == '__main__':
    main()
