
def main():
    n, m = map(int, input().split())
    K = collections.deque([None for _ in range(m)])
    A = [None for _ in range(m)]
    Af = [None for _ in range(m)]

    for i in range(m):
        K[i] = int(input())
        A[i] = collections.deque(list(map(int, input().split())))
        Af[i] = A[i][0]

    swi = 0
    for i in range(n):
        if Af[swi] is None:
            swi += 1
            continue
        target = Af[swi]
        e = [i for i, x in enumerate(Af) if x == target]
        if len(e) == 1:
            print('No')
            return
        ind = e[1]
        A[swi].popleft()
        Af[swi] = A[swi][0] if len(A[swi]) != 0 else None

        A[ind].popleft()
        Af[ind] = A[ind][0] if len(A[ind]) != 0 else None
        if len(A[swi]) == 0:
            swi += 1
        if swi == m + 1:
            break
    print('Yes')


if __name__ == '__main__':
    main()
