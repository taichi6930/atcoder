import collections


def main():
    n = int(input())
    D = {}
    for _ in range(n):
        d, s, t = map(int, input().split())
        if d - 1 not in D:
            D[d - 1] = collections.deque()
        for i in range(t - s):
            D[d - 1].append(s + i)
    DV = D.values()
    for dv in DV:
        C = collections.Counter(dv)
        if C.most_common()[0][1] > 1:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
