def main():
    k, n = map(int,  input().split())
    A = list(map(int,  input().split()))
    minA = 10 ** 7

    for i in range(n):
        minA = min(minA, A[i % n])


if __name__ == '__main__':
    main()
