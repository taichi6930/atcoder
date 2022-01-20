import heapq


def main():
    n, k = map(int, input().split())
    P = list(map(int, input().split()))

    Q = list(P[0: k])
    heapq.heapify(Q)
    print(min(Q))
    r = 0
    swi = False
    for i in range(n - k):
        if r != 0:
            heapq.heappush(Q, r)
        if swi:
            print(r)
            continue
        heapq.heappush(Q, P[k + i])
        heapq.heappop(Q)
        r = heapq.heappop(Q)
        print(r)
        if r == n - k + 1:
            swi = True


if __name__ == '__main__':
    main()
