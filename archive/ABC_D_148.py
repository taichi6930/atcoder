def main():
    n = int(input())
    A = list(map(int,  input().split()))
    k = 0

    if A.count(1) == 0:
        print(-1)
        return

    for i in range(n):
        if A[i] == k + 1:
            k += 1

    print(n - k)


if __name__ == '__main__':
    main()
