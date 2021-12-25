def main():
    n = int(input())
    A = [None for _ in range(n)]
    B = [None for _ in range(n)]
    TA = [None for _ in range(n)]

    for i in range(n):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
        TA[i] = a + b

    ans = - sum(A)



if __name__ == '__main__':
    main()
