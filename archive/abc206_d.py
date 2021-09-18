def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = []

    for i in range(n // 2 + 1):
        if i == n - i - 1:
            continue
        if A[i] != A[n - i - 1]:
            B.append(A[i])
            B.append(A[n - i - 1])
    print(max(len(set(B)) - 1, 0))


if __name__ == '__main__':
    main()
