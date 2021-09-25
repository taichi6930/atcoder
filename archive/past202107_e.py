from copy import copy


def main():

    n = int(input())
    n1 = copy(n)
    cnt1 = 0

    for i in range(100):
        if n1 % 3 != 0:
            cnt1 = i
            break
        n1 = n1 // 3

    cnt2 = 30 - cnt1
    n2 = 3 ** cnt2

    if n1 - n2 == 1 and cnt2 > 0:
        print(cnt2)
        return
    print(-1)


if __name__ == '__main__':
    main()
