import collections


def main():
    q = int(input())
    s = list()
    cnt = 0

    for i in range(q):
        q = list(map(str, input().split()))
        t = int(q[0])
        if t == 1:
            c, x = q[1], int(q[2])
            s += list(c * x)
            cnt += int(x)

        if t == 2:
            d = int(q[1])
            print(sum(list(map(lambda x: x ** 2,
                  list(collections.Counter(s[0: min(cnt, d)]).values())))))
            s = s[min(cnt, d):]
            cnt = min(cnt, d)


if __name__ == '__main__':
    main()
