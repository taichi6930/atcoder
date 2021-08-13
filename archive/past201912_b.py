def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    for i in range(n - 1):
        if A[i + 1] == A[i]:
            print('stay')
            continue
        if A[i + 1] > A[i]:
            print('up', A[i + 1] - A[i])
            continue
        print('down', - A[i + 1] + A[i])


if __name__ == '__main__':
    main()
