def main():
    n, x = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    XA = [None] * len(A)
    xx = 0 + x
    for i in range(n):
        k = xx // A[i]
        XA[i] = k
        xx -= k * A[i]

    cnt = 0

    for j in range(n - 1):

        if A[-2] - XA[j + 1] < XA[j + 1]:
            cnt += 1
        cnt += XA[j]
        XA[j + 1] = min(A[-2] - XA[j + 1], XA[j + 1])
    cnt += XA[n - 1]

    print(cnt)


if __name__ == '__main__':
    main()
