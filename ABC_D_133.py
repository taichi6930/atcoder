def main():
    n = int(input())
    A = list(map(int,  input().split()))
    k = [0] * (n + 1)
    for i in range(n):
        k[i] += A[i] // 2
        k[i + 1] += A[i] // 2
    print(k)


if __name__ == '__main__':
    main()
