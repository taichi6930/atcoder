def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    A1 = A[0::2]
    A2 = A[1::2]

    print("Yes" if sum(A2) - len(A2) + sum(A1) <= x else "No")


if __name__ == '__main__':
    main()
