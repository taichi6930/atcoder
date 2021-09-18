import collections


def main():
    topQ = None
    minQ = None
    ansQ = collections.deque()

    q = int(input())

    for i in range(q):
        w = list(map(int, input().split()))
        if len(w) == 2:
            x = w[1]
            topQ = x
            minQ = x if minQ is None else min(minQ, x)
            continue
        w = w[0]
        if w == 2:
            ansQ.append(topQ)
            continue
        if w == 3:
            topQ = minQ

    for j in list(ansQ):
        print(j)


if __name__ == '__main__':
    main()
